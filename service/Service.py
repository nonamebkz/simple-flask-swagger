class Service():
    def getName(self,name):
        result = {"status": True, "message": "success", "data": name}
        return result