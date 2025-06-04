from .models import Project, Task
from django_filters import rest_framework as filters



class TaskFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status',lookup_expr='exact')
    priority = filters.CharFilter(field_name='priority', lookup_expr='exact')
    assigned_to = filters.NumberFilter(field_name='assigned_to', lookup_expr='exact')

    