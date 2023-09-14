from drf_spectacular.utils import (OpenApiParameter,
                                   extend_schema, extend_schema_view)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.services import convert


@extend_schema_view(
    get=extend_schema(
        summary='Convert the currencies',
        parameters=[
            OpenApiParameter(name='from_currency', description='Currency to convert', type=str),
            OpenApiParameter(name='to_currency', description='Currency convert to', type=str),
            OpenApiParameter(name='amount', description='Amount to convert', type=float)
        ]
    )
)
class ConvertApiView(APIView):

    def get(self, request):
        from_currency = request.query_params.get('from_currency', None)
        to_currency = request.query_params.get('to_currency', None)
        amount = request.query_params.get('amount', None)
        if not from_currency or not to_currency or not amount:
            return Response({'detail': 'Missing required parameters.'}, status=status.HTTP_400_BAD_REQUEST)
        converted_amount = convert(from_currency, to_currency)
        return Response({'detail': f'{from_currency} to {to_currency} is successfully converted.',
                         'result': converted_amount}, status=status.HTTP_200_OK)


