import grpc
import location_pb2
import location_pb2_grpc

print("Updating sample payload..")


channel = grpc.insecure_channel("localhost:30020")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    latitude=17.673024132073149,
    longitude=167.03756982696303
)

response = stub.Create(location)
