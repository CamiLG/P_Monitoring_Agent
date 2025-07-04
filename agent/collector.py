from datetime import datetime
import platform
import psutil
import pytz


def get_processor_info():
    """Get processor information."""
    return platform.processor() or "Unknown Processor"

def get_running_processes():
    """Get a list of running processes."""
    return [proc.info for proc in psutil.process_iter(['pid', 'name', 'username'])]

def get_logged_in_users():
    """Get a list of logged-in users."""
    return [user.name for user in psutil.users()]

def get_os_name():
    """Get the operating system name."""
    return platform.system() or "Unknown OS"

def get_os_version():
    """Get the operating system version."""
    return platform.version() or "Unknown Version"

def get_timestamp():
    tz = pytz.timezone("America/Argentina/Buenos_Aires")
    return datetime.now(tz).isoformat()

def collect_data():
    return {
        "timestamp": get_timestamp(),
        "processor": get_processor_info(),
        "running_processes": get_running_processes(),
        "logged_in_users": get_logged_in_users(),
        "os_name": get_os_name(),    
        "os_version": get_os_version(),
    }
