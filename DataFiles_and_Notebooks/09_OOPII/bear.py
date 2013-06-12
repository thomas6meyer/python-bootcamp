import datetime
class Bear:
    logfile_name = "bear.log"
    bear_num     = 0
    def __init__(self,name):
        self.name = name
        print " made a bear called %s" % (name)
        self.logf  = open(Bear.logfile_name,"a")
        Bear.bear_num += 1
        self.my_num = Bear.bear_num
        self.logf.write("[%s] created bear #%i named %s\n" % \
                        (datetime.datetime.now(),Bear.bear_num,self.name))
        self.logf.flush()
    
    def growl(self,nbeep=5):
        print "\a"*nbeep

    def __del__(self):
        print "Bang! %s is no longer." % self.name
        self.logf.write("[%s] deleted bear #%i named %s\n" % \
                        (datetime.datetime.now(),self.my_num,self.name))
        self.logf.flush()
        # decrement the number of bears in the population
        Bear.bear_num -= 1
        # dont really need to close because Python will do the garbage collection
        #  for us. but it cannot hurt to be graceful here.
        self.logf.close()
