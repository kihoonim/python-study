from rediscluster import redis, RedisCluster
import data_pb2
import time

def main():
    r = redis.Redis(
        host='localhost', port=6379, db=0)
    key = 'key1'

    while True:
        try:
            k, get_data = r.brpop(key, timeout=10)
        
            if get_data != None:
                print(k)

                print(get_data)

                output_data1 = data_pb2.Data1()
                output_data1.ParseFromString(get_data)

                print(output_data1.value1)
                print(output_data1.value2)
                print(output_data1.value3)
                print(output_data1.value4)
                print(output_data1.value5)

            time.sleep(1)
            get_data = None
        except Exception as e:
            print(e)



if __name__ == '__main__':
    main()