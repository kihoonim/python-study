import basic_pb2


def main():
    message1 = basic_pb2.Messag1()
    message1.value1 = True
    message1.value2 = 'value2'
    message1.value3 = 100
    message1.value4 = 200
    message1.value5 = 10.5

    serialized_message = message1.SerializeToString()
    print(serialized_message)

    message1_des = basic_pb2.Messag1()

    message1_des.ParseFromString(serialized_message)

    print(message1_des)


if __name__ == '__main__':
    main()