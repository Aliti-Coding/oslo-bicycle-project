import hashlib


class UniqueId:
    """Generates unique id for each trip 
    """
    def __init__(self, start_station, end_station, start_time, end_time) -> None:
        super().__init__()
        self.start_station = start_station
        self.end_station = end_station
        self.start_time = start_time
        self.end_time = end_time
    def generate_id(self):
        input_string = f"{self.start_station}-{self.end_station}-{self.start_time}-{self.end_time}"

        hash_obj = hashlib.sha256(input_string.encode())
        hash_id = hash_obj.hexdigest()[:18]
        return hash_id

# test = UniqueId(start_station="test", end_station="never", start_time=221013, end_time=1200)

# print(type(test.generate_id()))