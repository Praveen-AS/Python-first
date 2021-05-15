import self as self

from Browser import scenarioTest

# scenarioTest.launchwebsite('firefox')
testInstance = scenarioTest()
testInstance.launchweb("https://www.goal.com")

testInstance.waitTime(20)

