import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    # filter by sender’s user_id
    sender = django_filters.UUIDFilter(field_name="sender__user_id", lookup_expr="exact")
    
    # filter by messages sent after a certain datetime
    sent_after = django_filters.IsoDateTimeFilter(field_name="sent_at", lookup_expr="gte")
    
    # filter by messages sent before a certain datetime
    sent_before = django_filters.IsoDateTimeFilter(field_name="sent_at", lookup_expr="lte")
    
    class Meta:
        model = Message
        fields = ["sender", "sent_after", "sent_before"]
