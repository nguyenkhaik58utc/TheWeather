import json

from django.shortcuts import render
from kafka import KafkaConsumer, TopicPartition


def index(request):
    # readfile = open("data.txt", "r")
    # lst = readfile.read().split('/')
    # nhietdo = float(lst[0])
    # doam = float(lst[1])
    # tocdogio = float(lst[2])
    # tamnhin = float(lst[3])
    # count = int(lst[4])
    # readfile.close()
    # consumer = KafkaConsumer(group_id='my-group', auto_offset_reset='latest',
    #                          bootstrap_servers="localhost:9092", enable_auto_commit=True)
    # topic_partition = TopicPartition(topic="Demo1", partition=0)
    # consumer.assign([topic_partition])
    # openfile = open("endOffset.txt", "r")
    #
    # consumer.seek(topic_partition, int(openfile.read()) + 1)
    # end_offset = consumer.end_offsets([topic_partition])[topic_partition]
    # for message in consumer:
    #     count += 1
    #     f = open("endOffset.txt", "w")
    #     f.write(str(message.offset))
    #     f.close()
    #     print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                          message.offset, message.key,
    #                                          message.value.decode()))
    #
    #     value = message.value.decode()
    #     abc = json.loads(value)
    #     nhietdo = ((nhietdo * (count - 1)) + abc['nhietDo']) / count
    #     doam = ((doam * (count - 1)) + abc['doAm']) / count
    #     tocdogio = ((tocdogio * (count - 1)) + abc['tocDoGio']) / count
    #     tamnhin = ((tamnhin * (count - 1)) + abc['tamNhin']) / count
    #     writeFile = open("data.txt", "w")
    #     writeFile.write(str(nhietdo) + "/" + str(doam) + "/" + str(tamnhin) + "/" + str(tocdogio) + "/" + str(count))
        context = {"viTri": "Hà Nội", "nhietDo": 35, "doAm": 80, "tocDoGio": 12,
                   "tamNhin": 7}
        return render(request, "ThoiTiet/index.html", context)
