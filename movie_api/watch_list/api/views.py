from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework import (
    generics,
    mixins
)

#loacal Imports
from watch_list.models import (
    WatchList,
    StreamPlatform,
    Review
)
from watch_list.api.serializers import(
    WatchListSerializer,
    StreamPlatformSerialzer,
    ReviewSerialzer
)

# GET AND POST METHOD FOR WATCH LIST
class WatchListAV(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
    def get(self, request, *args, **kwargs):
        
        try:
            watch_list = self.list(request,*args,**kwargs)
            return Response({
                'data':watch_list.data,
                'status':'Sucess'
            }, status=HTTP_200_OK)
        except ValidationError as ve:
            return Response({
                'status':'Failed',
                'errors':ve.detail
            }, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)    
    
    
    

 
    
    def post(self,request,*args,**kwargs):
        
        try:
            if len(request.data) == 0:
                return Response({
                    'status':'Failed'
                },status=HTTP_400_BAD_REQUEST)
            else:
                serializer = self.get_serializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'data':serializer.data,
                        'status':'Sucess'
                    })
                else:
                    return Response({
                     'status':'Failed',
                     'errors': serializer.errors  
                    })
                    
                
        except ValidationError as ve:
            return Response({
                'status':'Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)

# WATCH LIST SINGLE ITEM GET,DELETE, PATCH AND PUT

class WatchListDetailAV(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
    def get(self,request,*args,**kwargs):
        
      
            instance = self.retrieve(self,*args,**kwargs)
            return Response({
                'data':instance.data,
                'status':'Success'
            },status=HTTP_200_OK)
    
    def delete(self,request,*args,**kwargs):
        
        instance = self.get_object()
        
        self.perform_destroy(instance)
        
        return Response({
            'status':'Successful'
        },status=HTTP_200_OK)
    
    def put(self,request,*args,**kwargs):
        
        instance = self.get_object()
        serialzer = self.get_serializer(instance,data=request.data)
        
        if len(request.data) == 0:
            return Response({
                'status':'Failed'
            },status=HTTP_400_BAD_REQUEST)
        
        if serialzer.is_valid():
            serialzer.save()
            return Response({
                'status':'Success'
            },status=HTTP_200_OK)
        else:
            return Response({
                'status':'Failed',
                'errors':serialzer.errors
            },status=HTTP_400_BAD_REQUEST)
    
    def patch(self,request,*args,**kwargs):
        
        instance = self.get_object()
        serialzer = self.get_serializer(instance,data=request.data,partial=True)
        
        if len(request.data) == 0:
            return Response({
                
                'status':'Failed'
            },status=HTTP_400_BAD_REQUEST)
        
        
        if serialzer.is_valid():
            serialzer.save()
            return Response({
                'status':'Success'
            },status=HTTP_200_OK)
        else:
            return Response({
                'status':'Failed',
                'errors':serialzer.errors
            },status=HTTP_400_BAD_REQUEST)

# GET AND POST FOR PLATFORMS
class StreamPlatformListAV(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerialzer
    
    
    def get(self,request,*args,**kwargs):
        
        instance = self.list(request,*args,**kwargs)
        return Response({
            'data':instance.data,
            'status':"Success"
        },status=HTTP_200_OK)
    
    
    def post(self,request,*args,**kwargs):
        
        if len(request.data) == 0:
            return Response({
                'status':'Failed'
            },status=HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data':serializer.data
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Failed',
                    'errors':serializer.errors
                },status=HTTP_400_BAD_REQUEST)



# FOR Individual Platforms GET > PUT > PATH

class StreamPlatformDetailAV(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerialzer
    
    def get(self,request,*args,**kwargs):
        
        instance= self.retrieve(request,*args,**kwargs)
        
        return Response({
            'data':instance.data
        },status=HTTP_200_OK)
    
    def put(self,request,*args,**kwargs):
        
        if len(request.data) == 0:
            return Response({
                'status':'Failed'
                
            },status=HTTP_400_BAD_REQUEST)
        else:
            instance = self.get_object()
            serialzer = self.get_serializer(instance,data=request.data)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Success'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request,*args,**kwargs):
        
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({
            'status':'Success',
            'message':'Deleted Sucessfully'
        },status=HTTP_200_OK)
    
    
    def patch(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serialzer = self.get_serializer(instance, data=request.data, partial=True)
        
        if len(request.data) == 0:
            return Response({
                'status':'Failed'
            },status=HTTP_400_BAD_REQUEST)
        
        else:
            instance = self.get_object()
            serialzer = self.get_serializer(instance, data=request.data, partial=True)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
                
                


# Review Models Views

# FOR GET AND POST METHOD
class ReviewListAV(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzer
    
    def get(self,request,*args,**kwargs):
        
        try:
            instance = self.list(request,*args,**kwargs)
            return Response({
                'data': instance.data,
                'status':'Sucess'
            },status=HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            })
    
    def post(self,request,*args,**kwargs):
        
        try:
            
            if len(request.data) == 0:
                return Response({
                    'status':'Failed'
                },status=HTTP_400_BAD_REQUEST)
            
            serializer = self.get_serializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data':serializer.data,
                    'status':'Success'
                })
            else:
                return Response({
                    'status':'Failed',
                    'errors':serializer.errors
                })
            
        except ValidationError as ve:
            
            return Response({
                'status':'Failed',
                'errors':ve.detail
            })
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            })


# GET > DEL > PUT > PATCH 

class ReviewDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzer
    def get(self, request, *args, **kwargs):
        
        try:
            
            return Response({
                'data':self.retrieve(request,*args,**kwargs).data,
                'status' : 'Success'
            },status=HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors' : str(e)
                
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,*args,**kwargs):
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status':'Success',
            'msg':'Reccord Deleted'
        })
    
    def put(self,request, *args, **kwargs):
        
        try:
            instance = self.get_object()
            serialzer = self.get_serializer(instance, data=request.data)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data': serialzer.data,
                    'status' : 'Success'
                })
            else:
                return Response({
                    'status':'Failed',
                    'msg':' Failed To Update',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Failed to update',
                'errors':ve.detail
            }, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':"Failed",
                'msg':'Failed to update'
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
            