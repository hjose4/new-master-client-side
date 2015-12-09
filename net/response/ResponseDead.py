from traceback import print_exc
from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from panda3d.core import TransparencyAttrib

class ResponseDead(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            print "server sent dead guy:", self.username

            if self.worldMgr.isDDGame:
                print "isDDGame"
                if self.username in self.world.vehiclelist.keys():
                    vehicle = self.world.vehiclelist[self.username]
                    vehicle.props.health = vehicle.props.armor = 0
                    vehicle.isDead = True
                    vehicle.remove(self.world)
                    self.world.deadCounter +=1
                    #del self.world.vehiclelist[self.username]
                    print "deadCounter :",self.world.deadCounter
                    print "vehicle :",len(self.world.vehiclelist)
                    if self.world.deadCounter == len(self.world.vehiclelist)-1:
                        print "Last Man Standing"
                        self.world.gameEnd()
            else:  # for RR game
                if self.world.login == self.username:
                    print "you are dead"
                    self.world.vehicleContainer.isDead = True

                    # disable collision
                    # self.world.ignore('bullet-contact-added')

                    # set ghosting
                    self.world.vehicleContainer.chassisNP.setTransparency(TransparencyAttrib.MAlpha)
                    self.world.vehicleContainer.chassisNP.setAlphaScale(0.5)

                if self.username in self.world.vehiclelist.keys():
                    vehicle = self.world.vehiclelist[self.username]
                    vehicle.isDead = True
                    vehicle.remove()
                    del self.world.vehiclelist[self.username]
                    self.world.deadCounter += 1

                    print "deadCounter/vehiclelist :", self.world.deadCounter, "/", len(self.world.vehiclelist)

                    if self.world.deadCounter == len(self.world.vehiclelist)-1:
                        print "Last Man Standing"
                        self.world.gameEnd()


            print "ResponseDead - ",self.username

        except:
            self.log('Bad [' + str(Constants.SMSG_DEAD) + '] Dead Response')
            print_exc()
