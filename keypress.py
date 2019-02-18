import base64
import arcade
import requests



class MyGame(arcade.Window):
    """ Main application class. """


    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(800, 600, "Keys")

        # Don't show the mouse cursor
        self.set_mouse_visible(True)

        # BG
        self.line_start = -1

        # BG
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # move the background
        if self.line_start < 49:
            self.line_start += 1
        else:
            self.line_start = 0



    '''   
    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        #self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
    '''



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.ESCAPE:
            exit()

        print(key)

        # obfuscate!
        api_key = base64.standard_b64decode("VlRJVTJIMElCMkdWMkNXWQ==")
        url = "http://api.thingspeak.com/update?api_key={}&field1={}".format("VTIU2H0IB2GV2CWY", key)
        result = requests.get(url)

        #view with https://thingspeak.com/channels/621567





    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            print("Y")
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            print("X")


    def update(self, delta_time):
        """ Movement and game logic """






def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
