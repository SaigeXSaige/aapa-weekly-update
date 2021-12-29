import argparse
import sys
# Credit: https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
sys.path.append('./scripts')

from send_post import send_thread, send_init_post, send_reply_post, create_path

class CommandLine:
    def __init__(self):
        parser = argparse.ArgumentParser(description = "A script to post weekly AAPA Draft League results.")
        parser.add_argument(
            "-s", "--status_id", 
            help = "Id of the status to reply to (i.e. 12345678910)", 
            required = False, default = "")
        parser.add_argument(
            "-i", "--img_paths", 
            help = "List of paths to images separated by commas (i.e. /Desktop/rankings.png,/Desktop/stats.png,...)", 
            required = False, default = ""
        )
        parser.add_argument( ## get rid of this?
            "-f", "--full_img_paths",
            help = "Only use if paths to images are out of scope of your HOME directory (i.e. /Users/<other_username>/Desktop/rankings.png,...)", 
            required = False, default = ""
        )
        parser.add_argument(
            "-a", "--auto_thread", action = "store_true",
            help = "Posts entire thread using the list of image paths", 
            required = False, default = ""
        )

        argument = parser.parse_args()
        status = False

        if argument.auto_thread and argument.img_paths:
            print("Starting thread")
            img_paths = [create_path(img_path) for img_path in argument.img_paths.split(",")]
            print(img_paths)
            send_thread()
        if argument.status_id and argument.img_paths:
            print("Replying to post with id {0}\n".format(argument.status_id))
            img_paths = [create_path(img_path) for img_path in argument.img_paths.split(",")]
            print(img_paths)
            # send_reply_post(argument.status_id, argument.img_paths)
            status = True
        if argument.status_id and argument.full_img_paths:
            print("Replying to post with id {0}\n".format(argument.status_id))
            send_reply_post(argument.status_id, argument.full_img_paths)
            status = True
        if argument.img_paths:
            print("You have used '-i' or '--img_paths' with argument: {0}".format(argument.img_paths))
            img_paths = argument.img_paths.split(",")
            send_init_post(img_paths[0])
            status = True

        if not status:
            print("Please call -h for additional assistance") 


if __name__ == '__main__':
    app = CommandLine()