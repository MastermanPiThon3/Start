import pygame

class Stats:
    def __init__(self, fontColor, backgroundColor = None):
        pygame.font.init()
        self.Fired = 0
        self.Hits = 0
        self.Kills = 0
        self.Font = pygame.font.Font(None, 24)
        self.StartTime = pygame.time.get_ticks()
        self.LastUpdate = pygame.time.get_ticks()
        self.MaxFPS = 60
        self.FontColor = fontColor
        self.BgColor = backgroundColor

    def TimeUp(self):
        return 120000 < (pygame.time.get_ticks() - self.StartTime)

    def TimeString(self):
        gameTicks = pygame.time.get_ticks() - self.StartTime
        gameMinutes = gameTicks/60000
        gameSeconds = (gameTicks - (gameMinutes * 60000)) / 1000
        return "Time:   {0}:{1:02}".format(gameMinutes, gameSeconds)

    def Blit(self, arena, playerHealth):
        health = "Health: {0}".format(playerHealth)
        healthImage = self.Font.render(health, True, self.FontColor, self.BgColor)
        timeImage = self.Font.render(self.TimeString(), True, self.FontColor, self.BgColor)
        kills   = "Kills:  {0}".format(self.Kills)
        killsImage = self.Font.render (kills, True, self.FontColor, self.BgColor)

        healthPosition = [arena.Width - healthImage.get_width() - 10, 5]
        arena.Blit(healthImage, healthPosition)
        timePosition = [arena.Width - timeImage.get_width() - 10, healthPosition[1] + healthImage.get_height() + 5]
        arena.Blit(timeImage, timePosition)
        killsPosition = [arena.Width - killsImage.get_width() -10, timePosition[1] + timeImage.get_height() + 5]
        arena.Blit(killsImage, killsPosition)


    def FrameLimiter(self):
        msMinPerFrame = 1000 / self.MaxFPS
        msDelay = self.LastUpdate - pygame.time.get_ticks()
        if msDelay < msMinPerFrame:
            pygame.time.wait(msMinPerFrame - msDelay)

        self.LastUpdate = pygame.time.get_ticks()

        
