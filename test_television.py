from television import *
import pytest

class Test():
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

    def test_volume_up(self):
        # TV turned on, volumed increased, and muted
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'

        # TV turned on and unmuted
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [1]'

        # TV turned off and muted
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        # TV turned off and unmuted
        self.tv1.power()
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [1]'

    def test_channel_up(self):
        # TV is off and channel has been increased
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        # TV is on and channel increased by 1
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [1], Volume = [0]'

        # TV is on and increased past the maximum channel number.
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'

    def test_channel_down(self):
        # TV is off and channel decreased by one.
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        # TV is on and channel is decreased past the minimum.
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [3], Volume = [0]'

    def test_volume_up(self):
        # TV is off, volume increased
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        # TV is on, volume increased
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [1]'

        # TV is on, muted, volume increased
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [2]'

        # TV is on, and one has increased the volume past the maximum value
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [2]'

    def test_volume_down(self):
        # TV is off and volume is decreased
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        # TV is on and volume is decreased after the volume has been set to the max
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [1]'

        # TV is on, muted, and volume has been decreased.
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'

        # TV is decreased past the minimum value
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
