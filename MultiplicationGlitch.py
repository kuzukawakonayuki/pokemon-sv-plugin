import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

processingCount = 999
shortWait = 0.1
middleWait = 1
longWait = 2
screenWait = 3
itemNum = 0

class MultiplicationGlitch(JoycontrolPlugin):
    async def run(self):
        logger.info('processing start')
        count = 0
        while count < processingCount:
            MultiplicationGlitch.Reset()
            MultiplicationGlitch.ItemSet()
            MultiplicationGlitch.Multiplication()
            count += 1
        logger.info('done')

    @staticmethod
    async def Multiplication(self):
        commands = [
            {'button': 'a', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'a', 'wait': middleWait},
            {'button': 'a', 'wait': shortWait},
            {'button': 'a', 'wait': longWait},
            {'button': 'a', 'wait': shortWait},
            {'button': 'right', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'a', 'wait': screenWait},
            {'button': 'x', 'wait': shortWait},
            {'button': 'x', 'wait': shortWait},
            {'button': 'l', 'wait': shortWait},
            {'button': 'a', 'wait': middleWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'a', 'wait': middleWait},
            {'button': 'b', 'wait': screenWait},
            {'button': 'left', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
        ]
        for command in commands:
            await self.button_push(command['button'])
            await self.wait(command['wait'])

    @staticmethod
    async def ItemSet(self):
        await self.button_push('a')
        await self.wait(middleWait)
        await self.button_push('down')
        await self.wait(shortWait)
        await self.button_push('down')
        await self.wait(shortWait)
        await self.button_push('down')
        await self.wait(shortWait)
        await self.button_push('a')
        await self.wait(screenWait)
        num = 0
        while num < itemNum:
            await self.button_push('right')
            await self.wait(shortWait)
            num += 1
        await self.button_push('a')
        await self.wait(middleWait)
        await self.button_push('a')
        await self.wait(middleWait)
        await self.button_push('a')
        await self.wait(middleWait)
        await self.button_push('a')
        await self.wait(middleWait)
        await self.button_push('b')
        await self.wait(screenWait)

    @staticmethod
    async def Reset(self):
        i = 0
        while i < 20:
            await self.button_push('b')
            await self.wait(shortWait)
            i += 1
        await self.button_push('x')
        await self.wait(middleWait)
        await self.button_push('left')
        await self.wait(shortWait)
        await self.button_press('up')
        await self.wait(middleWait)
        await self.button_release('up')
        await self.wait(shortWait)