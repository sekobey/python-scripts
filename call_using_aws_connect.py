import boto3
import sys
import getopt


def main(argv):
    phoneNumber = ''
    message = ''

    try:
        opts, args = getopt.getopt(argv, "hp:m:", ["phone=", "message="])
    except getopt.GetoptError:
        print 'call.py -p <phone_number_in_E.164_format> -m <message_to_be_listened_in_call>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'call.py -p <phone_number_in_E.164_format> -m <message_to_be_listened_in_call>'
            sys.exit()
        elif opt in ("-p", "--phone"):
            phoneNumber = arg
        elif opt in ("-m", "--message"):
            message = arg

    print 'Destination Phone Number: ', phoneNumber
    print 'Message to be listened: ', message

    boto3.setup_default_session(profile_name='<your_profile>')

    client = boto3.client('connect')

    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber=phoneNumber,
        InstanceId='<your aws connect instance id>',
        QueueId='<queue id in your aws connect instance>',
        ContactFlowId='<contact flow id in your aws connect instance>',
        Attributes={
            'Message': message
        }
    )

    print "Response: ", response


if __name__ == "__main__":
    main(sys.argv[1:])
