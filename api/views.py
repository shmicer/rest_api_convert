from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.services import convert


@extend_schema_view(
    get=extend_schema(
        summary='GET request to convert between two currencies',
        parameters=[
            OpenApiParameter(name='from_currency', description='Currency to convert', type=str),
            OpenApiParameter(name='to_currency', description='Currency convert to', type=str),
            OpenApiParameter(name='amount', description='Amount to convert', type=float)
        ]
    )
)
class ConvertApiView(APIView):

    def get(self, request):
        from_currency = request.query_params.get('from_currency', None).upper()
        to_currency = request.query_params.get('to_currency', None).upper()
        amount = request.query_params.get('amount', None)
        if not from_currency or not to_currency or not amount:
            return Response({'detail': 'Missing required parameters.'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            amount = float(amount)
        except ValueError:
            return Response({'detail': 'Amount must be a valid number.'},
                            status=status.HTTP_400_BAD_REQUEST)
        converted_amount = format(convert(from_currency, to_currency) * amount,
                                  '.2f')
        return Response({'detail': f'{from_currency} to {to_currency} is successfully converted.',
                         'result': converted_amount}, status=status.HTTP_200_OK)
