from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
	message = 'This is not your client. So, mind your own business, buddy!'
	def has_object_permission(self,request, view, obj):
		return obj.user == request.user