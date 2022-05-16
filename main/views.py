from django.shortcuts import render
from django.views.generic import DetailView, View
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from main.models import Employee
from main.serializers import SerializerSearcherView


class SearcherView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.GET.get('employee'):
            if request.GET.get('select_all'):
                context['data'] = list(
                    Employee.objects.filter(employee__icontains=request.GET.get('employee')).values())
                context['keys'] = [field.name for field in Employee._meta.get_fields()]
                # print('123')

            else:
                keys = list(request.GET.keys())
                context['data'] = list(
                    Employee.objects.filter(employee__icontains=request.GET.get('employee')).values(*keys))
                context['keys'] = keys
        # print(context)

        return render(request, 'search.html', context)


class SearcherViewSerializers(ListModelMixin, GenericAPIView):
    serializer_class = SerializerSearcherView

    def get_queryset(self):
        queryset = Employee.objects.all()
        employee_name = self.request.query_params.get('employee')
        if employee_name:
            queryset = queryset.filter(employee=employee_name)
        return queryset

    def get(self, request):
        return self.list(request)

# class SearcherViewSerializers(ListModelMixin):
#     def get(self, request):
#         employee = Employee.objects.all()
#         serializer = SerializerSearcherView(employee, many=True)
#         return Response(serializer.data)
