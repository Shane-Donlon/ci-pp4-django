from django_tables2 import tables, LinkColumn
from report_swarm.models import ReportSwarmCase

from django_tables2.utils import A  

class ticketTable(tables.Table):
    id = LinkColumn('ticketView', text=lambda record:record.id, args=[A('pk')], attrs={
        "a": {"style": "color: #0055f2;"} })
    class Meta:
        model = ReportSwarmCase
        exclude = ["description","image"]
        row_attrs = {
            "data-assignee": lambda record: record.assignee
        }
