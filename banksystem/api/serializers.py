from rest_framework import serializers 

from .models import * 



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name','address','branch_code',)
        read_only_fields = ('id',)

class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')


class BankSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    class Meta:
        model = Bank 
        fields = ('__all__')


class ClientManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientManager
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()
    class Meta:
        model = Account
        fields = ('__all__')



class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')