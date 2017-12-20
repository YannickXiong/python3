from locust import HttpLocust, TaskSet, task
import json

# http://www.cnblogs.com/LanTianYou/p/5987741.html#_label0


class UserBehavior(TaskSet):

    # Execute before any task
    def on_start(self):
        pass

    # one task with an optional argument, weight
    @task(1)
    def api_query(self):
        # just give the router, and using locust -H to refer to a host a domain.
        # r = self.client.get("/api/nodes/show.json?name=python")
        # if json.loads(r.content)["id"] != "90":
        # for python3, r.content returns a byte object.
        # if json.loads(r.content.decode())["id"] != 90:
        #     r.failure("Got wrong response, id=" + r.content.decode())
        # else:
        #     r.success("Verify Ok!")

        # In order to be able to use the response object as a context manager (with the with statement),
        # you have to set the catch_response keyword argument to True
        with self.client.get("/api/nodes/show.json?name=python", catch_response=True) as response:
            if response.content == "":
                response.failure("No data")
            if json.loads(response.content.decode())["id"] != 90:
                response.failure("Got wrong response, id=" + response.content.decode())
            else:
                # response.success("Verify oK") # this is python2, in python3, no arguments.
                response.success()


class WebUserLocust(HttpLocust):
    weight = 1
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
