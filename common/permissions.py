from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
	message = 'This is not your client. So, mind your own business, buddy!'
	def has_object_permission(self,request, view, obj):
		return obj.user == request.user

class IsLoggedInWithSameUsername(BasePermission):
	message = 'You cannot edit profiles besides your own.'
	def has_object_permission(self, request, view, obj):
		return obj.id == request.user.id