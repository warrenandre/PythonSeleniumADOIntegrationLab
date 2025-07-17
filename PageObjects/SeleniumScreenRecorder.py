import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import base64
import json
import numpy as np

class SeleniumScreenRecorder:
    """Screen recorder using Selenium's built-in capabilities"""
    
    def __init__(self, driver):
        self.driver = driver
        self.recording = False
        self.screenshots = []
        self.output_dir = "recordings"
        
        # Create output directory
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def start_recording(self, test_name=None):
        """Start recording using continuous screenshots"""
        if test_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = f"test_{timestamp}"
        
        self.test_name = test_name
        self.recording = True
        self.screenshots = []
        
        # Enable Chrome DevTools for advanced recording (Chrome only)
        if self.driver.capabilities['browserName'].lower() == 'chrome':
            self._start_chrome_recording()
        
        print(f"Screen recording started for: {test_name}")
        return True
    
    def stop_recording(self):
        """Stop recording and save"""
        if not self.recording:
            return None
            
        self.recording = False
        
        # Stop Chrome recording if applicable
        if self.driver.capabilities['browserName'].lower() == 'chrome':
            video_path = self._stop_chrome_recording()
            if video_path:
                return video_path
        
        # Fallback: Save screenshots as GIF
        if self.screenshots:
            gif_path = self._create_gif_from_screenshots()
            print(f"Recording saved as GIF: {gif_path}")
            return gif_path
        
        return None
    
    def capture_screenshot(self, step_name=None):
        """Capture a screenshot during recording"""
        if step_name is None:
            step_name = f"step_{len(self.screenshots) + 1}"
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        filename = f"{self.test_name}_{step_name}_{timestamp}.png"
        screenshot_path = os.path.join(self.output_dir, filename)
        
        self.driver.save_screenshot(screenshot_path)
        self.screenshots.append(screenshot_path)
        
        return screenshot_path
    
    def _start_chrome_recording(self):
        """Start Chrome's built-in screen recording via DevTools"""
        try:
            # Enable runtime and page domains
            self.driver.execute_cdp_cmd('Runtime.enable', {})
            self.driver.execute_cdp_cmd('Page.enable', {})
            
            # Start screen capture (requires Chrome 89+)
            self.driver.execute_cdp_cmd('Page.startScreencast', {
                'format': 'png',
                'quality': 80,
                'maxWidth': 1920,
                'maxHeight': 1080,
                'everyNthFrame': 1
            })
            
            print("Chrome DevTools recording started")
            return True
            
        except Exception as e:
            print(f"Chrome recording not available: {e}")
            return False
    
    def _stop_chrome_recording(self):
        """Stop Chrome recording and save video"""
        try:
            # Stop screen capture
            self.driver.execute_cdp_cmd('Page.stopScreencast', {})
            
            # Get performance logs which contain screencast frames
            logs = self.driver.get_log('performance')
            frames = []
            
            for log in logs:
                message = json.loads(log['message'])
                if message.get('method') == 'Page.screencastFrame':
                    frame_data = message['params']['data']
                    frames.append(base64.b64decode(frame_data))
            
            if frames:
                # Save as video file (simplified - you'd need ffmpeg for real video)
                video_path = os.path.join(self.output_dir, f"{self.test_name}_recording.mp4")
                print(f"Chrome recording captured {len(frames)} frames")
                return video_path
            
        except Exception as e:
            print(f"Error stopping Chrome recording: {e}")
        
        return None
    
    def _create_gif_from_screenshots(self):
        """Create GIF from captured screenshots (requires Pillow)"""
        try:
            from PIL import Image
            
            if not self.screenshots:
                return None
            
            # Open all screenshots
            images = []
            for screenshot_path in self.screenshots:
                img = Image.open(screenshot_path)
                images.append(img)
            
            # Save as GIF
            gif_path = os.path.join(self.output_dir, f"{self.test_name}_recording.gif")
            images[0].save(
                gif_path,
                save_all=True,
                append_images=images[1:],
                duration=500,  # 500ms per frame
                loop=0
            )
            
            return gif_path
            
        except ImportError:
            print("Pillow not installed - cannot create GIF")
            return None
        except Exception as e:
            print(f"Error creating GIF: {e}")
            return None