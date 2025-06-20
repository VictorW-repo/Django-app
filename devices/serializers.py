import base64
from rest_framework import serializers
from .models import Device, Payload


class PayloadSerializer(serializers.Serializer):
    fCnt = serializers.IntegerField()
    devEUI = serializers.CharField(max_length=16)
    raw_data = serializers.CharField()

    def validate_devEUI(self, value):
        if len(value) != 16:
            raise serializers.ValidationError("devEUI must be exactly 16 characters")
        return value

    def create(self, validated_data):
        # Get or create device
        device, _ = Device.objects.get_or_create(devEUI=validated_data['devEUI'])
        
        # Decode base64 to hex
        try:
            decoded_bytes = base64.b64decode(validated_data['raw_data'])
            decoded_hex = decoded_bytes.hex()
        except Exception:
            raise serializers.ValidationError("Invalid base64 encoding")
        
        # Determine status
        status = 'passing' if decoded_hex == '01' else 'failing'
        
        # Create payload
        payload = Payload.objects.create(
            device=device,
            fCnt=validated_data['fCnt'],
            raw_data=validated_data['raw_data'],
            decoded_data=decoded_hex,
            status=status
        )
        
        # Update device status
        device.latest_status = status
        device.save()
        
        return payload

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'devEUI': instance.device.devEUI,
            'fCnt': instance.fCnt,
            'status': instance.status,
            'decoded_data': instance.decoded_data,
            'created_at': instance.created_at.isoformat()
        }