class Television:
    '''
    Minimum and Maximum volumes/ channels
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''

        Turn the power on/off
        '''
        if self.__status == True:
            self.__status = False

        elif self.__status == False:
            self.__status = True

    def mute(self):
        '''
        Mute and unmute the TV volume
        '''

        if self.__status == False:
            return

        if self.__muted == True:
            self.__muted = False

        elif self.__muted == False:
            self.__muted = True

    def channel_up(self):
        '''Turn the tv channel up 1. Resets TV to minimum channel if TV is on max channel'''
        if self.__status == False:
            return
        elif self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self):
        '''Turn the tv channel down by 1. Resets TV to maximum channel if TV is on minimum channel'''
        if self.__status == False:
            return
        elif self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self):
        '''Increase TV volume'''
        if self.__status == False:
            return

        self.__muted = False
        if self.__volume == Television.MAX_VOLUME:
            pass

        else:
            self.__volume += 1

    def volume_down(self):
        '''Turn down TV volume by 1.'''
        if self.__status == False:
            return

        self.__muted = False
        if self.__volume == Television.MIN_VOLUME:
            pass
        else:
            self.__volume -= 1

    def __str__(self):
        '''return: the status of the television, the volume, and the current channel.'''
        if self.__muted == True:
            return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [0]'

        return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]'