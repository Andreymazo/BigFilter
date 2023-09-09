import datetime

from django.shortcuts import render
from .models import Modalities, Studies, StudiesTable
import names
import random
from datetime import timedelta
import uuid
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from big_filter.filters import StudiesFilter


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def init_db(request):
    """
    База предоставляется уже предзаполненной, но в случае желания перехода
    на другую СУБД, можно раскомментировать код ниже и сгенерировать тестовые данные.
    """

    # Modalities.objects.all().delete()
    # modalities = [['CT', 'Computed Tomography'],
    #               ['MR', 'Magnetic Resonance'],
    #               ['PT', 'Positron emission tomography'],
    #               ['US', 'Ultrasound'],
    #               ['XA', 'X-Ray Angiography'],
    #               ['MG', 'Mammography'],
    #               ['CR', 'Computed Radiography'],
    #               ['AS', 'Angioscopy'],
    #               ['DX', 'Digital Radiography'],
    #               ['EC', 'Echocardiography']]
    # for modality in modalities:
    #     modality_obj = Modalities()
    #     modality_obj.short_code = modality[0]
    #     modality_obj.name = modality[1]
    #     modality_obj.save()
    # for i in range(100000):
    #     study_obj = Studies()
    #     study_obj.patient_fio = names.get_full_name()
    #     study_obj.patient_birthdate = random_date(datetime.datetime(2000, 1, 1, 0, 0, 0),
    #                                               datetime.datetime(2023, 1, 1, 0, 0, 0))
    #     study_obj.study_date = random_date(datetime.datetime(2023, 1, 1, 0, 0, 0),
    #                                        datetime.datetime(2023, 9, 1, 0, 0, 0))
    #     study_obj.study_uid = uuid.uuid4()

class TableListView(FilterView, SingleTableView):
    model = Studies
    table_class = StudiesTable
    filterset_class = StudiesFilter
    # generate_values()
    template_name = "big_filter/first.html"
    # ordering = ('distance',)  # quantity, name
    table_pagination = {"per_page": 10}
    
    # def get_queryset(self, **kwargs):
    #     """
    #     Return the list of items for this view.

    #     The return value must be an iterable and may be an instance of
    #     `QuerySet` in which case `QuerySet` specific behavior will be enabled.
    #     """
    #     if self.request.method == "GET":

    #         if self.queryset is not None:
    #             queryset = self.queryset
    #             if isinstance(queryset, QuerySet):
    #                 queryset = queryset.all()
    #         if self.model is not None:
    #             queryset = self.model._default_manager.all()
    #         else:
    #             raise ImproperlyConfigured(
    #                 "%(cls)s is missing a QuerySet. Define "
    #                 "%(cls)s.model, %(cls)s.queryset, or override "
    #                 "%(cls)s.get_queryset()." % {"cls": self.__class__.__name__}
    #             )
    #         ordering = self.get_ordering()
    #         if ordering:
    #             if isinstance(ordering, str):
    #                 ordering = (ordering,)
    #             queryset = queryset.order_by(*ordering)
    #     Modalities.objects.all().delete()
    #     modalities = [['CT', 'Computed Tomography'],
    #               ['MR', 'Magnetic Resonance'],
    #               ['PT', 'Positron emission tomography'],
    #               ['US', 'Ultrasound'],
    #               ['XA', 'X-Ray Angiography'],
    #               ['MG', 'Mammography'],
    #               ['CR', 'Computed Radiography'],
    #               ['AS', 'Angioscopy'],
    #               ['DX', 'Digital Radiography'],
    #               ['EC', 'Echocardiography']]
    #     for modality in modalities:
    #         modality_obj = Modalities()
    #         modality_obj.short_code = modality[0]
    #         modality_obj.name = modality[1]
    #         modality_obj.save()
            
    #         # big_filter_studies
    #         # truncate big_filter_studies restart identity cascade;
    #     for i in range(100000):
    #         study_obj = Studies()
    #         study_obj.patient_fio = names.get_full_name()
    #         study_obj.patient_birthdate = random_date(datetime.datetime(2000, 1, 1, 0, 0, 0),
    #                                                 datetime.datetime(2023, 1, 1, 0, 0, 0))
    #         study_obj.study_uid = uuid.uuid4()
    #         study_obj.study_date = random_date(datetime.datetime(2023, 1, 1, 0, 0, 0),
    #                                         datetime.datetime(2023, 9, 1, 0, 0, 0))
    #         study_obj.study_modality = Modalities.objects.all().first()
            
    #         study_obj.save()
        # Values_table.objects.all().delete()

        # for i in range(1, 100):
            # generate_values()

        # return queryset

    # return render(request, 'big_filter/first.html', context)

