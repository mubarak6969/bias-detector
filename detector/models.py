from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MLModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='models/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    bias_score = models.FloatField(null=True, blank=True)
    fairness_metrics = models.JSONField(null=True, blank=True)  # Store metrics as JSON
    report_file = models.FileField(upload_to='bias_reports/', null=True, blank=True)

    def __str__(self):
        return f"Test for {self.ml_model.name} on {self.dataset.name}"