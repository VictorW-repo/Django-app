from django.db import models


class Device(models.Model):
    devEUI = models.CharField(max_length=16, unique=True, db_index=True)
    latest_status = models.CharField(
        max_length=10,
        choices=[('passing', 'Passing'), ('failing', 'Failing')],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Device {self.devEUI} - {self.latest_status or 'No status'}"


class Payload(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='payloads')
    fCnt = models.IntegerField()
    raw_data = models.CharField(max_length=255)
    decoded_data = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=[('passing', 'Passing'), ('failing', 'Failing')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['device', 'fCnt']
        ordering = ['-created_at']

    def __str__(self):
        return f"Payload {self.fCnt} from {self.device.devEUI} - {self.status}"