import datetime
import uuid
from redis_om import HashModel, Migrator, Field
from redis import Redis


class Tracking(HashModel):
    date: datetime.date
    file: str = Field(index=True)
    seq: int = Field(index=True)
    num_files: int

    class Meta:
        database = Redis(host="localhost", port=6379, password="")


def producer():
    track = Tracking(
        date=datetime.date.today(), file=str(uuid.uuid1()), seq=1, num_files=3
    )
    print("#### PRODUCER RECORD: " + str(track))
    track.save()
    consumer(track.pk)


def consumer(pk):
    Migrator().run()
    result = Tracking.find(Tracking.pk == pk).all()
    print("#### CONSUMER QUERY: " + str(result))


producer()
