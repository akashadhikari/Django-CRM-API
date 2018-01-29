from rest_framework import serializers

from .models import (
    AddClient,
    ListOfProduct
    )

class ListOfProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfProduct
        fields = (
            'user',
            'user_name',
            'client',
            'client_name',
            'service_name',
            'service_detail')

class AddClientSerializer(serializers.ModelSerializer):

    # not adding (many=True) will result in id selection only

    client_listofproduct = ListOfProductSerializer(many=True)

    class Meta:
        model = AddClient
        fields = (
            'id',
            'user',
            'client_name',
            'organisation_name',
            'employee_size',
            'address',
            'phone_number',
            'email_org',
            'introduction',
            'ownership_type',
            'client_value',
            'created',
            'logo',
            'designation',
            'mobile_no_head',
            'email_head',
            'social_media_id_head',
            'full_name',
            'designation_contactperson',
            'office_phone',
            'mobile_no',
            'email',
            'social_media_id',
            'reference_website',
            'facebook_id',
            'linked_in_id',
            'pan_no',
            'billing_name',
            'outflowed_to',
            'service_outflowed',
            'outflow_date',
            'amount',
            'client_listofproduct',
            'branch_incharge',
            'branch_address',
            'branch_phone',
            'branch_email',
            )

    def create(self, validated_data):
        listofproduct_data = validated_data.pop('client_listofproduct')
        addclient = AddClient.objects.create(**validated_data)
        for each in listofproduct_data:
            ListOfProduct.objects.create(addclient=addclient, **each)
        return addclient

    def update(self, instance, validated_data):
        instance.client_name = validated_data.get('client_name', instance.client_name)
        instance.organisation_name = validated_data.get('organisation_name', instance.organisation_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email_org = validated_data.get('email_org', instance.email_org)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.ownership_type = validated_data.get('ownership_type', instance.ownership_type)
        instance.employee_size = validated_data.get('employee_size', instance.employee_size)
        instance.client_value = validated_data.get('client_value', instance.client_value)
        instance.created = validated_data.get('created', instance.created)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.mobile_no_head = validated_data.get('mobile_no_head', instance.mobile_no_head)
        instance.email_head = validated_data.get('email_head', instance.email_head)
        instance.social_media_id_head = validated_data.get('social_media_id_head', instance.social_media_id_head)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.designation_contactperson = validated_data.get('designation_contactperson', instance.designation_contactperson)
        instance.office_phone = validated_data.get('office_phone', instance.office_phone)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.email = validated_data.get('email', instance.email)
        instance.social_media_id = validated_data.get('social_media_id', instance.social_media_id)
        instance.reference_website = validated_data.get('reference_website', instance.reference_website)
        instance.facebook_id = validated_data.get('facebook_id', instance.facebook_id)
        instance.linked_in_id = validated_data.get('linked_in_id', instance.linked_in_id)
        instance.pan_no = validated_data.get('pan_no', instance.pan_no)
        instance.billing_name = validated_data.get('billing_name', instance.billing_name)
        instance.outflowed_to = validated_data.get('outflowed_to', instance.outflowed_to)
        instance.service_outflowed = validated_data.get('service_outflowed', instance.service_outflowed)
        instance.outflow_date = validated_data.get('outflow_date', instance.outflow_date)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.branch_incharge = validated_data.get('branch_incharge', instance.branch_incharge)
        instance.branch_address = validated_data.get('branch_address', instance.branch_address)
        instance.branch_phone = validated_data.get('branch_phone', instance.branch_phone)
        instance.branch_email = validated_data.get('branch_email', instance.branch_email)
        instance.save()

        client_listofproduct = validated_data.get('client_listofproduct')

        if client_listofproduct:
            for each in client_listofproduct:
                product_id = each.get('id', None)
                if product_id:
                    client_prod = ListOfProduct.objects.get(id=product_id, client=instance)
                    client_prod.client = each.get('client', client_prod.client)
                    client_prod.service_name = each.get('service_name', client_prod.service_name)
                    client_prod.service_detail = each.get('service_detail', client_prod.service_detail)
                    client_prod.duration = each.get('duration', client_prod.duration)

                    client_prod.save()
                else:
                    ListOfProduct.objects.create(account=instance, **each)

        return instance

class StatsSerializer(serializers.ModelSerializer):

    today_created = serializers.ReadOnlyField()
    yesterday_created = serializers.ReadOnlyField()
    this_week_created = serializers.ReadOnlyField()
    this_month_created = serializers.ReadOnlyField()
    this_year_created = serializers.ReadOnlyField()

    class Meta:
        model = AddClient
        fields = ('today_created', 'yesterday_created', 'this_week_created', 'this_month_created', 'this_year_created')
