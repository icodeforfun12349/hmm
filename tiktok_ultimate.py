"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                      TIKTOK ULTIMATE AUTOMATION                           ║
║                    Professional Grade Engagement Tool                     ║
║                         by @Crypted - v2.0                                ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, 
    StaleElementReferenceException, ElementClickInterceptedException
)
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
import uuid
import time
import threading
import os
import sys
from datetime import datetime
from queue import Queue

# Rich library for beautiful TUI
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.live import Live
    from rich.layout import Layout
    from rich import box
    from rich.text import Text
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
    from rich.align import Align
    from rich.style import Style as RichStyle
    from rich.markup import escape
    USE_RICH = True
    console = Console()
except ImportError:
    print("Installing required dependencies...")
    os.system(f"{sys.executable} -m pip install rich webdriver-manager selenium requests --quiet --break-system-packages")
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.live import Live
    from rich.layout import Layout
    from rich import box
    from rich.text import Text
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
    from rich.align import Align
    from rich.style import Style as RichStyle
    from rich.markup import escape
    USE_RICH = True
    console = Console()


class UltimateBot:
    """Combined Zefoy + Zefame automation with stunning UI"""
    
    def __init__(self):
        # Browser setup
        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-logging")
        self.options.add_argument("--log-level=3")
        self.options.add_argument("--silent")
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        self.driver = None
        self.service = Service(ChromeDriverManager().install())
        self.user_agent_index = 0
        
        # List of user agents to rotate
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        ]
        
        # Threading control
        self.vignette_checker_running = False
        self.should_close_vignette = True
        self.zefoy_running = False
        self.zefame_running = False
        
        # Statistics
        self.stats = {
            'zefoy_success': 0,
            'zefoy_failed': 0,
            'zefame_success': 0,
            'zefame_failed': 0,
            'zefoy_total': 0,
            'zefame_total': 0,
            'start_time': None
        }
        
        # Message queue for thread-safe console updates
        self.message_queue = Queue()
        
        # Zefoy XPaths
        self.xpaths = [
            "/html/body/div[6]/div/div[2]/div/div/div[2]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[3]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[4]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[5]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[6]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[7]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[8]/div/button"
        ]
        self.xpathsWithAd = [
            "/html/body/div[6]/div/div[2]/div/div/div[2]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[3]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[4]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[6]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[7]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[8]/div/button",
            "/html/body/div[6]/div/div[2]/div/div/div[9]/div/button"
        ]
        self.enter_video_url = [
            "/html/body/div[7]/div/form/div/input",
            "/html/body/div[8]/div/form/div/input",
            "/html/body/div[9]/div/form/div/input",
            "/html/body/div[10]/div/form/div/input",
            "/html/body/div[11]/div/form/div/input",
            "/html/body/div[12]/div/form/div/input",
            "/html/body/div[13]/div/form/div/input"
        ]
        self.timer_text = [
            "/html/body/div[7]/div/div/span",
            "/html/body/div[8]/div/div/span",
            "/html/body/div[9]/div/div/span",
            "/html/body/div[10]/div/div/span",
            "/html/body/div[11]/div/div/span",
            "/html/body/div[12]/div/div/span",
            "/html/body/div[13]/div/div/span"
        ]
        self.search_button = [
            "/html/body/div[7]/div/form/div/div/button",
            "/html/body/div[8]/div/form/div/div/button",
            "/html/body/div[9]/div/form/div/div/button",
            "/html/body/div[10]/div/form/div/div/button",
            "/html/body/div[11]/div/form/div/div/button",
            "/html/body/div[12]/div/form/div/div/button",
            "/html/body/div[13]/div/form/div/div/button"
        ]
        self.send_button = [
            "/html/body/div[7]/div/div/div[1]/div/form/button",
            "/html/body/div[8]/div/div/div[1]/div/form/button",
            "/html/body/div[9]/div/div/div[1]/div/form/button",
            "/html/body/div[10]/div/div/div[1]/div/form/button",
            "/html/body/div[11]/div/div/div[1]/div/form/button",
            "/html/body/div[12]/div/div/div[1]/div/form/button",
            "/html/body/div[13]/div/div/div[1]/div/form/button"
        ]
        
        # Service names
        self.zefoy_names = ["Followers", "Hearts", "Comment Hearts", "Views", "Shares", "Favorites", "Livestream"]
        self.zefame_names = {
            229: "Views",
            228: "Followers", 
            232: "Likes",
            235: "Shares",
            236: "Favorites"
        }
        
        # User selections
        self.selected_services = []  # [(service_type, service_info, amount), ...]
        self.video_url = ""
        self.video_id = ""
        self.zefoy_initialized = False
        
    def clear_screen(self):
        """Clear terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_next_user_agent(self):
        """Get next user agent from rotation"""
        ua = self.user_agents[self.user_agent_index]
        self.user_agent_index = (self.user_agent_index + 1) % len(self.user_agents)
        return ua
    
    def flush_dns(self):
        """Flush DNS cache"""
        try:
            if os.name == 'nt':  # Windows
                os.system('ipconfig /flushdns > nul 2>&1')
            else:  # Linux/Mac
                os.system('sudo systemd-resolve --flush-caches > /dev/null 2>&1 || sudo killall -HUP mDNSResponder > /dev/null 2>&1')
        except:
            pass
    
    def restart_browser(self):
        """Restart browser with new user agent and flushed DNS"""
        self.message_queue.put(('warn', "Restarting browser with new identity..."))
        
        try:
            # Close current browser
            if self.driver:
                self.driver.quit()
                time.sleep(2)
            
            # Flush DNS
            self.flush_dns()
            
            # Create new options with new user agent
            self.options = Options()
            self.options.add_argument("--disable-notifications")
            self.options.add_argument("--disable-logging")
            self.options.add_argument("--log-level=3")
            self.options.add_argument("--silent")
            self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            # Add new user agent
            new_ua = self.get_next_user_agent()
            self.options.add_argument(f'user-agent={new_ua}')
            
            # Start new browser
            self.driver = webdriver.Chrome(service=self.service, options=self.options)
            
            self.message_queue.put(('info', f"Browser restarted with new user agent"))
            
            # Re-initialize Zefoy
            return self.reinitialize_zefoy_silent()
            
        except Exception as e:
            self.message_queue.put(('error', f"Browser restart failed: {str(e)}"))
            return False
    
    def reinitialize_zefoy_silent(self):
        """Re-initialize Zefoy after browser restart (silent mode for dashboard)"""
        try:
            # Navigate to Zefoy
            self.driver.get("https://zefoy.com/")
            
            # Wait for page load
            if not self.check_loaded('ua-check', 10):
                return False
            
            self.message_queue.put(('info', "Zefoy page loaded - solve CAPTCHA if needed"))
            
            # Wait for CAPTCHA
            if not self.check_loaded('row', 100):
                return False
            
            self.message_queue.put(('success', "CAPTCHA solved"))
            
            # Handle ads (silent)
            self.should_close_vignette = False
            time.sleep(1)
            
            if self.click_ad_button():
                self.message_queue.put(('warn', "Ad detected - watch and close it manually"))
                # Don't block here, user will handle it
                time.sleep(30)  # Give user time to watch ad
            
            self.should_close_vignette = True
            self.message_queue.put(('success', "Zefoy re-initialized successfully"))
            
            return True
            
        except Exception as e:
            self.message_queue.put(('error', f"Zefoy re-init failed: {str(e)}"))
            return False
    
    def show_splash(self):
        """Show beautiful startup splash screen"""
        self.clear_screen()
        
        logo = """
    ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗
    ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
       ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ 
       ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ 
       ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗
       ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
        """
        
        splash = Panel(
            Align.center(
                f"[bold cyan]{logo}[/bold cyan]\n\n"
                "[bold white]ULTIMATE AUTOMATION[/bold white]\n"
                "[dim]Professional Grade Engagement Tool[/dim]\n\n"
                "[yellow]●[/yellow] Zefoy Integration  [yellow]●[/yellow] Zefame Integration\n"
                "[yellow]●[/yellow] Dual-Service Support  [yellow]●[/yellow] Real-time Statistics\n\n"
                "[dim italic]by @Crypted - v2.0[/dim italic]"
            ),
            border_style="cyan",
            box=box.DOUBLE,
            padding=(1, 2)
        )
        
        console.print(splash)
        time.sleep(2)
    
    def show_header(self, title=""):
        """Display minimal header"""
        if title:
            console.print(f"\n[bold cyan]━━━ {title} [/bold cyan]" + "[cyan]" + "━" * (70 - len(title) - 5) + "[/cyan]")
        else:
            console.print("[bold cyan]TikTok Ultimate[/bold cyan] [dim]│ Professional Automation Suite[/dim]")
    
    def login(self):
        """Beautiful login screen"""
        self.clear_screen()
        
        login_panel = Panel(
            "[bold cyan]◆ AUTHENTICATION REQUIRED ◆[/bold cyan]\n\n"
            "[dim]Please enter your credentials to continue[/dim]",
            border_style="cyan",
            box=box.ROUNDED,
            padding=(1, 2)
        )
        
        console.print(login_panel)
        console.print()
        
        max_attempts = 3
        for attempt in range(max_attempts):
            username = console.input("[cyan]→[/cyan] Username: ").strip()
            password = console.input("[cyan]→[/cyan] Password: ").strip()
            
            if username == "admin" and password == "admin":
                console.print("\n[green]✓[/green] Authentication successful")
                
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[cyan]Initializing browser engine..."),
                    console=console
                ) as progress:
                    task = progress.add_task("init", total=None)
                    self.driver = webdriver.Chrome(service=self.service, options=self.options)
                    progress.update(task, completed=True)
                
                console.print("[green]✓[/green] Browser ready")
                time.sleep(1)
                return True
            else:
                remaining = max_attempts - attempt - 1
                console.print(f"\n[red]✗[/red] Invalid credentials")
                if remaining > 0:
                    console.print(f"[yellow]![/yellow] {remaining} attempt(s) remaining\n")
        
        console.print("\n[red]✗[/red] Access denied")
        return False
    
    def fetch_zefame_services(self):
        """Fetch available Zefame services"""
        try:
            response = requests.get("https://zefame-free.com/api_free.php?action=config", timeout=10)
            data = response.json()
            services = data.get('data', {}).get('tiktok', {}).get('services', [])
            return services
        except:
            return []
    
    def display_service_selection(self):
        """Beautiful service selection menu"""
        self.clear_screen()
        self.show_header("SERVICE SELECTION")
        
        console.print("\n[bold white]Select services to run simultaneously:[/bold white]\n")
        
        # Zefoy services
        zefoy_table = Table(
            title="[bold cyan]ZEFOY SERVICES[/bold cyan]",
            box=box.ROUNDED,
            border_style="cyan",
            show_header=True,
            header_style="bold cyan"
        )
        zefoy_table.add_column("#", style="dim", width=4)
        zefoy_table.add_column("Service", style="white", width=20)
        zefoy_table.add_column("Status", width=12)
        zefoy_table.add_column("Rate", style="dim", width=25)
        
        for i, name in enumerate(self.zefoy_names, 1):
            zefoy_table.add_row(
                f"Z{i}",
                name,
                "[green]●[/green] ONLINE",
                "~25 per cycle"
            )
        
        console.print(zefoy_table)
        console.print()
        
        # Zefame services
        zefame_services = self.fetch_zefame_services()
        if zefame_services:
            zefame_table = Table(
                title="[bold magenta]ZEFAME SERVICES[/bold magenta]",
                box=box.ROUNDED,
                border_style="magenta",
                show_header=True,
                header_style="bold magenta"
            )
            zefame_table.add_column("#", style="dim", width=4)
            zefame_table.add_column("Service", style="white", width=20)
            zefame_table.add_column("Status", width=12)
            zefame_table.add_column("Rate", style="dim", width=25)
            
            for i, service in enumerate(zefame_services, 1):
                sid = service.get('id')
                name = self.zefame_names.get(sid, service.get('name', '').strip())
                available = service.get('available', False)
                status = "[green]●[/green] ONLINE" if available else "[red]●[/red] OFFLINE"
                rate = service.get('description', '').strip()
                
                zefame_table.add_row(
                    f"F{i}",
                    name,
                    status,
                    rate if rate else "Variable"
                )
            
            console.print(zefame_table)
        
        console.print(f"\n[dim]Enter service codes separated by commas (e.g., Z1,F2,Z4)[/dim]")
        console.print(f"[dim]Or press Enter to use all available services[/dim]\n")
        
        selection = console.input("[cyan]→[/cyan] Select services: ").strip()
        
        if not selection:
            # Use all services
            for i in range(len(self.zefoy_names)):
                self.selected_services.append(('zefoy', i, None))
            for service in zefame_services:
                if service.get('available'):
                    self.selected_services.append(('zefame', service, None))
        else:
            # Parse selection
            codes = [c.strip().upper() for c in selection.split(',')]
            for code in codes:
                if code.startswith('Z') and code[1:].isdigit():
                    idx = int(code[1:]) - 1
                    if 0 <= idx < len(self.zefoy_names):
                        self.selected_services.append(('zefoy', idx, None))
                elif code.startswith('F') and code[1:].isdigit():
                    idx = int(code[1:]) - 1
                    if 0 <= idx < len(zefame_services):
                        self.selected_services.append(('zefame', zefame_services[idx], None))
        
        if not self.selected_services:
            console.print("\n[red]✗[/red] No services selected")
            return False
        
        console.print(f"\n[green]✓[/green] Selected {len(self.selected_services)} service(s)")
        time.sleep(1)
        return True
    
    def get_target_config(self):
        """Get target amounts for each service"""
        self.clear_screen()
        self.show_header("TARGET CONFIGURATION")
        
        console.print("\n[bold white]Configure target amounts for each service:[/bold white]\n")
        
        updated_services = []
        for service_type, service_info, _ in self.selected_services:
            if service_type == 'zefoy':
                service_name = self.zefoy_names[service_info]
            else:
                sid = service_info.get('id')
                service_name = self.zefame_names.get(sid, service_info.get('name', ''))
            
            while True:
                try:
                    amount = console.input(f"[cyan]→[/cyan] {service_name}: ")
                    if amount.strip() == "":
                        amount = 1000  # Default
                    else:
                        amount = int(amount)
                    if amount > 0:
                        break
                    console.print("[red]✗[/red] Must be positive")
                except ValueError:
                    console.print("[red]✗[/red] Must be a number")
            
            updated_services.append((service_type, service_info, amount))
        
        self.selected_services = updated_services
        
        console.print(f"\n[green]✓[/green] Configuration complete")
        time.sleep(1)
        return True
    
    def get_video_url_input(self):
        """Get video URL"""
        self.clear_screen()
        self.show_header("VIDEO TARGET")
        
        console.print("\n[bold white]Enter TikTok video URL:[/bold white]\n")
        
        self.video_url = console.input("[cyan]→[/cyan] URL: ").strip()
        
        # Parse video ID for Zefame
        try:
            response = requests.post(
                "https://zefame-free.com/api_free.php?",
                data={"action": "checkVideoId", "link": self.video_url},
                timeout=10
            )
            self.video_id = response.json().get("data", {}).get("videoId", "")
            console.print(f"\n[green]✓[/green] Video ID: {self.video_id}")
        except:
            console.print("\n[yellow]![/yellow] Could not parse video ID (Zefame services may not work)")
        
        time.sleep(1)
        return True
    
    def initialize_zefoy(self):
        """Initialize Zefoy connection"""
        console.print("\n[cyan]→[/cyan] Connecting to Zefoy...")
        
        self.driver.get("https://zefoy.com/")
        self.start_vignette_checker()
        
        # Wait for page load
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ua-check'))
            )
            console.print("[green]✓[/green] Zefoy loaded")
        except TimeoutException:
            console.print("[red]✗[/red] Zefoy connection timeout")
            return False
        
        time.sleep(1)
        
        # Wait for CAPTCHA
        console.print("[cyan]→[/cyan] Waiting for CAPTCHA...")
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'row'))
            )
            console.print("[green]✓[/green] CAPTCHA solved")
        except TimeoutException:
            console.print("[red]✗[/red] CAPTCHA timeout")
            return False
        
        # Handle ads
        self.handle_zefoy_ad()
        
        return True
    
    def handle_zefoy_ad(self):
        """Handle Zefoy ads"""
        self.should_close_vignette = False
        
        try:
            btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-rewarded-ad-button"))
            )
            if "View a short ad" in self.driver.page_source:
                console.print("\n[yellow]![/yellow] Ad detected - please watch and close manually")
                btn.click()
                console.input("\n[cyan]→[/cyan] Press Enter when ad is closed: ")
        except:
            pass
        
        self.should_close_vignette = True
    
    def start_vignette_checker(self):
        """Background thread to close popups"""
        self.vignette_checker_running = True
        thread = threading.Thread(target=self._vignette_checker_loop, daemon=True)
        thread.start()
    
    def _vignette_checker_loop(self):
        """Background loop to close ads"""
        while self.vignette_checker_running:
            try:
                if self.should_close_vignette:
                    self.close_google_vignette()
            except:
                pass
            time.sleep(2)
    
    def close_google_vignette(self):
        """Try to close Google ads"""
        try:
            selectors = [
                "button[aria-label='Close ad']",
                "div[id*='google_image_div'] button",
                "#dismiss-button"
            ]
            
            for selector in selectors:
                try:
                    btn = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if btn.is_displayed():
                        btn.click()
                        return True
                except:
                    continue
        except:
            pass
        return False
    
    def robust_click(self, xpath, timeout=10, max_retries=3, silent=False):
        """Robust click with multiple fallback methods"""
        for attempt in range(max_retries):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                
                try:
                    element.click()
                    return True
                except (ElementClickInterceptedException, Exception):
                    pass
                
                try:
                    element = self.driver.find_element(By.XPATH, xpath)
                    element.send_keys(Keys.ENTER)
                    return True
                except Exception:
                    pass
                
                try:
                    element = self.driver.find_element(By.XPATH, xpath)
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    time.sleep(0.5)
                    self.driver.execute_script("arguments[0].click();", element)
                    return True
                except Exception:
                    pass
                    
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
                pass
                
            if attempt < max_retries - 1:
                time.sleep(2)
        
        return False
    
    def check_rate_limit(self):
        """Check if rate limit message is present"""
        try:
            rate_limit_texts = [
                "Too many requests",
                "Please slow down",
                "Rate limit",
                "Try again later"
            ]
            
            page_text = self.driver.page_source.lower()
            for text in rate_limit_texts:
                if text.lower() in page_text:
                    return True
            return False
        except:
            return False
    
    def check_long_rate_limit(self):
        """Check for long rate limit (e.g., 'Please wait 525592 minute(s)')"""
        try:
            import re
            page_source = self.driver.page_source
            
            # Look for patterns like "Please wait X minute(s)" where X > 1000
            match = re.search(r'Please wait (\d+) minute', page_source, re.IGNORECASE)
            if match:
                minutes = int(match.group(1))
                # If more than 1000 minutes (unrealistic), it's a long rate limit
                if minutes > 1000:
                    return True, minutes
            
            return False, 0
        except:
            return False, 0
    
    def wait_for_rate_limit(self):
        """Wait when rate limited"""
        self.message_queue.put(('warn', "Rate limit detected - waiting 60 seconds..."))
        time.sleep(60)
        return True
    
    def check_loaded(self, classname, timeout):
        """Check if page element loaded"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, classname))
            )
            return True
        except TimeoutException:
            return False
    
    def run_zefoy_service(self, service_idx, target_amount):
        """Run a Zefoy service"""
        service_name = self.zefoy_names[service_idx]
        current_amount = 0
        
        # Click service button
        if not self.robust_click(self.xpaths[service_idx]):
            self.message_queue.put(('error', f"Zefoy {service_name}: Failed to select"))
            return
        
        time.sleep(2)
        
        # Enter video URL
        try:
            elem = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.enter_video_url[service_idx]))
            )
            elem.send_keys(self.video_url)
            time.sleep(1)
        except:
            self.message_queue.put(('error', f"Zefoy {service_name}: URL input failed"))
            return
        
        # Click search
        if not self.robust_click(self.search_button[service_idx]):
            self.message_queue.put(('error', f"Zefoy {service_name}: Search failed"))
            return
        
        time.sleep(2)
        
        # Click send
        if not self.robust_click(self.send_button[service_idx]):
            pass  # Timer check will handle this
        
        self.message_queue.put(('info', f"Zefoy {service_name}: Started"))
        
        # Main loop
        while current_amount < target_amount:
            try:
                # Check for long rate limit BEFORE waiting
                is_long_limit, minutes = self.check_long_rate_limit()
                if is_long_limit:
                    self.message_queue.put(('warn', f"Zefoy {service_name}: Long rate limit detected ({minutes} min) - restarting browser..."))
                    
                    # Restart browser
                    if self.restart_browser():
                        self.message_queue.put(('success', f"Zefoy {service_name}: Browser restarted - re-configuring service..."))
                        
                        # Re-select service and configure
                        time.sleep(2)
                        if not self.robust_click(self.xpaths[service_idx]):
                            self.message_queue.put(('error', f"Zefoy {service_name}: Failed to re-select service"))
                            return
                        
                        time.sleep(2)
                        self.check_loaded('row', 5)
                        
                        # Re-enter video URL
                        try:
                            elem = WebDriverWait(self.driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, self.enter_video_url[service_idx]))
                            )
                            elem.send_keys(self.video_url)
                            time.sleep(1)
                        except:
                            self.message_queue.put(('error', f"Zefoy {service_name}: Failed to re-enter URL"))
                            return
                        
                        # Re-click search and send
                        if not self.robust_click(self.search_button[service_idx], timeout=5):
                            self.message_queue.put(('error', f"Zefoy {service_name}: Failed to re-search"))
                            return
                        
                        time.sleep(3)
                        self.robust_click(self.send_button[service_idx], timeout=10)
                        
                        self.message_queue.put(('success', f"Zefoy {service_name}: Resumed after browser restart"))
                        continue
                    else:
                        self.message_queue.put(('error', f"Zefoy {service_name}: Browser restart failed"))
                        return
                
                # Wait for timer
                WebDriverWait(self.driver, 900).until(
                    EC.text_to_be_present_in_element(
                        (By.XPATH, self.timer_text[service_idx]),
                        "Next Submit: READY....!"
                    )
                )
                time.sleep(3)
                
                # Check for rate limit before attempting
                if self.check_rate_limit():
                    self.wait_for_rate_limit()
                    continue
                
                # Search
                if self.robust_click(self.search_button[service_idx], timeout=8, silent=True):
                    time.sleep(2)
                    
                    # Send
                    if self.robust_click(self.send_button[service_idx], timeout=10):
                        current_amount += 25
                        self.stats['zefoy_success'] += 1
                        self.stats['zefoy_total'] += 25
                        self.message_queue.put(('success', f"Zefoy {service_name}: +25 ({current_amount}/{target_amount})"))
                    else:
                        self.stats['zefoy_failed'] += 1
                        self.message_queue.put(('warn', f"Zefoy {service_name}: Send failed"))
                else:
                    self.stats['zefoy_failed'] += 1
                    self.message_queue.put(('warn', f"Zefoy {service_name}: Search failed"))
                
            except TimeoutException:
                self.message_queue.put(('error', f"Zefoy {service_name}: Timeout"))
                break
        
        self.message_queue.put(('success', f"Zefoy {service_name}: Complete"))
    
    def run_zefame_service(self, service_info, target_amount):
        """Run a Zefame service"""
        sid = service_info.get('id')
        service_name = self.zefame_names.get(sid, service_info.get('name', ''))
        current_amount = 0
        
        self.message_queue.put(('info', f"Zefame {service_name}: Started"))
        
        while current_amount < target_amount and self.zefame_running:
            try:
                response = requests.post(
                    "https://zefame-free.com/api_free.php?action=order",
                    data={
                        "service": sid,
                        "link": self.video_url,
                        "uuid": str(uuid.uuid4()),
                        "videoId": self.video_id
                    },
                    timeout=15
                )
                
                result = response.json()
                
                # Check for success - handle both English and French responses
                is_success = False
                message = result.get('message', '').lower()
                
                # French: "Commande passée avec succès" or "commande passée avec succès"
                # English: status == 'success'
                if result.get('status') == 'success' or 'succès' in message or 'success' in message or 'commande passée' in message:
                    is_success = True
                    amount = result.get('data', {}).get('amount', 0)
                    
                    # If amount is 0, try to parse from response
                    if amount == 0:
                        # Some services might return different structure
                        amount = result.get('amount', 0)
                    
                    # Still 0? Use a default increment
                    if amount == 0:
                        amount = 10  # Default increment for Zefame
                    
                    current_amount += amount
                    self.stats['zefame_success'] += 1
                    self.stats['zefame_total'] += amount
                    self.message_queue.put(('success', f"Zefame {service_name}: +{amount} ({current_amount}/{target_amount})"))
                else:
                    self.stats['zefame_failed'] += 1
                    error = result.get('message', 'Unknown error')
                    # Only show error if it's not just "waiting"
                    if 'wait' not in error.lower() and 'attend' not in error.lower():
                        self.message_queue.put(('warn', f"Zefame {service_name}: {error}"))
                
                # Wait for next available
                wait_time = result.get("data", {}).get("nextAvailable")
                if wait_time:
                    try:
                        wait_time = float(wait_time)
                        if wait_time > time.time():
                            sleep_duration = wait_time - time.time() + 1
                            time.sleep(sleep_duration)
                    except:
                        time.sleep(60)  # Default wait
                else:
                    time.sleep(60)
                    
            except Exception as e:
                self.stats['zefame_failed'] += 1
                self.message_queue.put(('error', f"Zefame {service_name}: {str(e)}"))
                time.sleep(60)
        
        self.message_queue.put(('success', f"Zefame {service_name}: Complete"))
    
    def create_stats_panel(self):
        """Create real-time statistics panel"""
        if self.stats['start_time']:
            elapsed = int(time.time() - self.stats['start_time'])
            hours, remainder = divmod(elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            runtime = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            runtime = "00:00:00"
        
        total_success = self.stats['zefoy_success'] + self.stats['zefame_success']
        total_failed = self.stats['zefoy_failed'] + self.stats['zefame_failed']
        total_delivered = self.stats['zefoy_total'] + self.stats['zefame_total']
        
        success_rate = 0
        if total_success + total_failed > 0:
            success_rate = (total_success / (total_success + total_failed)) * 100
        
        stats_content = (
            f"[bold cyan]RUNTIME[/bold cyan]     {runtime}\n"
            f"[bold green]DELIVERED[/bold green]   {total_delivered:,}\n"
            f"[bold yellow]SUCCESS[/bold yellow]     {total_success} cycles\n"
            f"[bold red]FAILED[/bold red]      {total_failed} cycles\n"
            f"[bold magenta]RATE[/bold magenta]        {success_rate:.1f}%"
        )
        
        return Panel(
            stats_content,
            title="[bold white]STATISTICS[/bold white]",
            border_style="white",
            box=box.ROUNDED,
            padding=(1, 2)
        )
    
    def create_services_panel(self):
        """Create active services panel"""
        services_table = Table(box=box.SIMPLE, show_header=True, header_style="bold white")
        services_table.add_column("Service", style="cyan", width=20)
        services_table.add_column("Type", style="dim", width=10)
        services_table.add_column("Status", width=15)
        
        for service_type, service_info, amount in self.selected_services:
            if service_type == 'zefoy':
                name = self.zefoy_names[service_info]
                stype = "Zefoy"
            else:
                sid = service_info.get('id')
                name = self.zefame_names.get(sid, 'Unknown')
                stype = "Zefame"
            
            status = "[green]●[/green] Running"
            services_table.add_row(name, stype, status)
        
        return Panel(
            services_table,
            title="[bold white]ACTIVE SERVICES[/bold white]",
            border_style="white",
            box=box.ROUNDED,
            padding=(0, 1)
        )
    
    def run_automation(self):
        """Main automation loop with live dashboard"""
        self.stats['start_time'] = time.time()
        self.zefoy_running = True
        self.zefame_running = True
        
        # Start all service threads
        threads = []
        
        for service_type, service_info, amount in self.selected_services:
            if service_type == 'zefoy':
                thread = threading.Thread(
                    target=self.run_zefoy_service,
                    args=(service_info, amount),
                    daemon=True
                )
            else:
                thread = threading.Thread(
                    target=self.run_zefame_service,
                    args=(service_info, amount),
                    daemon=True
                )
            
            threads.append(thread)
            thread.start()
            time.sleep(2)  # Stagger starts
        
        # Live dashboard
        self.clear_screen()
        
        with Live(console=console, refresh_per_second=2, screen=False) as live:
            while any(t.is_alive() for t in threads):
                # Create layout
                layout = Table.grid(expand=True)
                layout.add_column()
                layout.add_column()
                
                # Header
                header = Panel(
                    "[bold cyan]TIKTOK ULTIMATE[/bold cyan] [dim]│ Live Dashboard[/dim]",
                    border_style="cyan",
                    box=box.ROUNDED
                )
                
                # Stats and services
                stats_panel = self.create_stats_panel()
                services_panel = self.create_services_panel()
                
                # Messages
                messages = []
                while not self.message_queue.empty():
                    try:
                        msg_type, msg_text = self.message_queue.get_nowait()
                        color_map = {
                            'success': 'green',
                            'error': 'red',
                            'warn': 'yellow',
                            'info': 'cyan'
                        }
                        color = color_map.get(msg_type, 'white')
                        messages.append(f"[{color}]●[/{color}] {msg_text}")
                    except:
                        break
                
                # Keep last 10 messages
                messages = messages[-10:]
                
                messages_panel = Panel(
                    "\n".join(messages) if messages else "[dim]Waiting for activity...[/dim]",
                    title="[bold white]ACTIVITY LOG[/bold white]",
                    border_style="white",
                    box=box.ROUNDED,
                    padding=(1, 2),
                    height=14
                )
                
                # Build layout
                top_row = Table.grid(expand=True)
                top_row.add_column(ratio=1)
                top_row.add_column(ratio=1)
                top_row.add_row(stats_panel, services_panel)
                
                final_layout = Table.grid(expand=True)
                final_layout.add_row(header)
                final_layout.add_row("")
                final_layout.add_row(top_row)
                final_layout.add_row("")
                final_layout.add_row(messages_panel)
                
                live.update(final_layout)
                time.sleep(0.5)
        
        # Wait for all threads
        for thread in threads:
            thread.join()
        
        self.show_completion()
    
    def show_completion(self):
        """Show beautiful completion screen"""
        self.clear_screen()
        
        total_delivered = self.stats['zefoy_total'] + self.stats['zefame_total']
        total_success = self.stats['zefoy_success'] + self.stats['zefame_success']
        total_failed = self.stats['zefoy_failed'] + self.stats['zefame_failed']
        
        success_rate = 0
        if total_success + total_failed > 0:
            success_rate = (total_success / (total_success + total_failed)) * 100
        
        elapsed = int(time.time() - self.stats['start_time'])
        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        completion = Panel(
            Align.center(
                "[bold green]✓ MISSION COMPLETE ✓[/bold green]\n\n"
                f"[white]Total Delivered:[/white] [bold cyan]{total_delivered:,}[/bold cyan]\n"
                f"[white]Success Rate:[/white] [bold green]{success_rate:.1f}%[/bold green]\n"
                f"[white]Runtime:[/white] [bold yellow]{hours:02d}:{minutes:02d}:{seconds:02d}[/bold yellow]\n\n"
                f"[dim]Zefoy: {self.stats['zefoy_success']} success, {self.stats['zefoy_failed']} failed[/dim]\n"
                f"[dim]Zefame: {self.stats['zefame_success']} success, {self.stats['zefame_failed']} failed[/dim]\n\n"
                "[bold white]Thank you for using TikTok Ultimate[/bold white]"
            ),
            border_style="green",
            box=box.DOUBLE,
            padding=(2, 4)
        )
        
        console.print(completion)
    
    def main(self):
        """Main entry point"""
        try:
            # Splash
            self.show_splash()
            
            # Login
            if not self.login():
                return
            
            # Service selection
            if not self.display_service_selection():
                return
            
            # Target configuration
            if not self.get_target_config():
                return
            
            # Video URL
            if not self.get_video_url_input():
                return
            
            # Initialize Zefoy
            self.clear_screen()
            self.show_header("INITIALIZATION")
            
            if not self.initialize_zefoy():
                console.print("\n[red]✗[/red] Failed to initialize Zefoy")
                return
            
            console.print("[green]✓[/green] All systems ready")
            time.sleep(2)
            
            # Run automation
            self.run_automation()
            
        except KeyboardInterrupt:
            console.print("\n\n[yellow]![/yellow] Interrupted by user")
        finally:
            self.zefoy_running = False
            self.zefame_running = False
            self.vignette_checker_running = False
            
            if self.driver:
                self.driver.quit()
            
            console.print("\n[dim]Goodbye![/dim]\n")


if __name__ == "__main__":
    bot = UltimateBot()
    bot.main()
