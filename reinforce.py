rooms_events = { 'data': 
    { 'rooms': 
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],

    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}


# for key, value in rooms_events.items():
#     print(value)
#     print(type(value))
    

room_201 = rooms_events['data']['rooms'][0]['capacity']
print(room_201)



# room_201_events = []
for data in rooms_events['data']['events']:
    if data['room_id'] == 1: 
        if data['attendees'] <= room_201:
            print('ok') 



