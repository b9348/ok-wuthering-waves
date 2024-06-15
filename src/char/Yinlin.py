from ok.logging.Logger import get_logger

from src.char.BaseChar import BaseChar

logger = get_logger(__name__)


class Yinlin(BaseChar):
    def do_perform(self):
        if self.is_forte_full():
            if self.liberation_available():
                self.click_liberation()
                self.sleep(3.1)
            self.heavy_attack()
            self.sleep(0.4)
        elif self.resonance_available():
            self.click_resonance()
            self.sleep(0.2)
            if self.liberation_available():
                self.click_liberation()
                self.sleep(3.1)
            else:
                self.sleep(0.2)
            self.click_resonance()
            self.sleep(.6)
        elif self.echo_available():
            echo_key = self.get_echo_key()
            self.task.send_key_down(echo_key)
            self.sleep(.8)
            self.switch_next_char(post_action=self.echo_post_action)
        elif self.liberation_available():
            self.click_liberation()
            self.sleep(3.1)
        self.switch_next_char()

    def echo_post_action(self):  # hold down the echo for 1 seconds and switch and then release the echo key
        self.task.send_key_up(self.get_echo_key())
        self.sleep(0.01)
