from rediscluster import redis, RedisCluster
import data_pb2

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)

    input_data1 = data_pb2.Data1()
    input_data1.value1 = True
    input_data1.value2 = 'value2'
    set_data = input_data1.SerializeToString()
    print(set_data)

    key = 'key'
    r.set(key, set_data)
    get_data = r.get(key)
    
    print(get_data)

    output_data1 = data_pb2.Data1()
    output_data1.ParseFromString(get_data)

    print(output_data1.value1)
    print(output_data1.value2)

if __name__ == '__main__':
    main()