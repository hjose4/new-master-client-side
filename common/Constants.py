# define Constants

class Constants:
    RAND_INT                            = 1
    RAND_STRING                         = 2
    RAND_SHORT                          = 3
    RAND_FLOAT                          = 4

    SERVER_IP                           = 'csproject.calstatela.edu' # csproject.calstatela.edu # also need to change config.json
    SERVER_PORT                         = 9252
    DEBUG                               = True
    MSG_NONE                            = 0

    CMSG_LOGIN                          = 101
    CMSG_DISCONNECT                     = 102
    CMSG_REGISTER                       = 103
    CMSG_FORGOT_PASSWORD                = 104
    CMSG_CREATE_CHARACTER               = 105
    CMSG_CHAT                           = 106
    CMSG_MOVE                           = 107
    CMSG_POWER_UP                       = 108
    CMSG_POWER_UP_PICK_UP               = 109
    CMSG_HEALTH 						= 110
    CMSG_ENTER_LOBBY                    = 111
    CMSG_ENTER_GAME_LOBBY               = 112
    CMSG_ENTER_GAME_NAME                = 113
    CMSG_CREATE_LOBBY                   = 114
    CMSG_PRIVATE_CHAT                   = 115
    CMSG_INVITE                         = 116
    CMSG_CAR_CHOICE                     = 117
    CMSG_CAR_PAINT                      = 118
    CMSG_CAR_TIRES                      = 119
    CMSG_GARAGE_DETAILS                 = 120
    CMSG_GARAGE_PURCHASE                = 121
    CMSG_RESULTS                        = 122
    CMSG_RANKINGS                       = 123
    CMSG_PRIZES                         = 124
    CMSG_COLLISION                      = 125
    CMSG_DEAD                           = 126
    CMSG_READY                          = 127
    CMSG_SET_POSITION                   = 128
    CMSG_TIME                           = 129
    CMSG_SET_RANK                       = 130
    CMSG_CHECKPOINTS                    = 133
    CMSG_CURRENCY                       = 134
    REQ_HEARTBEAT                       = 301
    CMSG_REQ_TEST                       = 160

    SMSG_LOGIN                          = 201
    SMSG_DISCONNECT                     = 202
    SMSG_REGISTER                       = 203
    SMSG_FORGOT_PASSWORD                = 204
    SMSG_CREATE_CHARACTER               = 205
    SMSG_CHAT                           = 206
    SMSG_MOVE                           = 207
    SMSG_POWER_UP                       = 208
    SMSG_POWER_UP_PICK_UP               = 209
    SMSG_CHANGE_HEALTH 					= 210
    SMSG_ENTER_LOBBY                    = 211
    SMSG_ENTER_GAME_LOBBY               = 212
    SMSG_ENTER_GAME_NAME                = 213
    SMSG_CREATE_LOBBY                   = 214
    SMSG_PRIVATE_CHAT                   = 215
    SMSG_INVITE                         = 216
    SMSG_CAR_CHOICE                     = 217
    SMSG_CAR_PAINT                      = 218
    SMSG_CAR_TIRES                      = 219
    SMSG_GARAGE_DETAILS                 = 220
    SMSG_GARAGE_PURCHASE                = 221
    SMSG_RESULTS                        = 222
    SMSG_RANKINGS                       = 223
    SMSG_PRIZES                         = 224
    SMSG_COLLISION                      = 225
    SMSG_DEAD                           = 226
    SMSG_READY                          = 227
    SMSG_SET_POSITION                   = 228
    SMSG_TIME                           = 229
    SMSG_SET_RANK                       = 230
    SMSG_SET_READY                      = 231
    SMSG_CURRENCY                       = 234
    SMSG_RENDER_CHARACTER               = 310
    SMSG_REMOVE_CHARACTER               = 311


    MAX_HEALTH = {
        "1": 250,
        "2": 200,
        "3": 150,
        "4": 125,
    }
    VEHICLE_HEALTH = {
        "1": 200,
        "2": 170,
        "3": 100,
        "4": 175,
    }

    MAX_WEIGHT = {
        "1": 1500,
        "2": 550,
        "3": 400,
        "4": 350,
    }
    MAX_ARMOR = {
        "1": 375,
        "2": 300,
        "3": 225,
        "4": 250,
    }

    MAX_WHEEL = {
        "1": 1050,
        "2": 1750,
        "3": 3250,
        "4": 3600,
    }

    MAX_BRAKE = {
        "1": 100,
        "2": 100,
        "3": 100,
        "4": 100,
    }

    MAX_SPEED = {
        "1": 30,
        "2": 35,
        "3": 45,
        "4": 500,
    }
