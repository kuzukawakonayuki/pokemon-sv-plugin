import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

processingCount = 9999
shortWait = 0.15
middleWait = 1
longWait = 2
screenWait = 2.5
itemNum = 1
itemLength = 6

class MultiplicationGlitch(JoycontrolPlugin):
    async def run(self):
        logger.info('processing start')
        count = 0
        nowLength = 0
        while count < processingCount:
            await MultiplicationGlitch.Reset(self)
            #await MultiplicationGlitch.ItemSet(self, nowLength)
            await MultiplicationGlitch.Multiplication(self)
            count += 1
            # resetItemLength
            #if nowLength < itemLength:
            #    nowLength += 1
            #else:
            #    nowLength = 0
        logger.info('done')

    async def Multiplication(self):
        commands = [
            {'button': 'a', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'a', 'wait': longWait},
            {'button': 'a', 'wait': middleWait},
            {'button': 'a', 'wait': longWait},
            {'button': 'a', 'wait': middleWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'right', 'wait': shortWait},
            {'button': 'a', 'wait': screenWait},
            {'button': 'x', 'wait': shortWait},
            {'button': 'x', 'wait': shortWait},
            {'button': 'l', 'wait': shortWait},
            {'button': 'a', 'wait': middleWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'up', 'wait': shortWait},
            {'button': 'a', 'wait': middleWait},
            #{'button': 'b', 'wait': screenWait},
            #{'button': 'left', 'wait': shortWait},
            #{'button': 'up', 'wait': shortWait},
        ]
        for command in commands:
            await self.button_push(command['button'])
            await self.wait(command['wait'])

    async def ItemSet(self, length):
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

        # setItemNum
        num = 0
        while num < itemNum:
            await self.button_push('right')
            await self.wait(shortWait)
            num += 1

        # setItemLength
        while length < itemLength:
            await self.button_push('down')
            await self.wait(shortWait)
            length += 1

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