from hardware_agent.utils import Platform

if Platform.is_android():
    from jnius import autoclass
    from android import mActivity
else:
    autoclass  = lambda *args: args


class AndroidServiceAgent:

    def __init__(self) -> None:
        self.setup_service()

    @Platform.android
    def setup_service(self) -> bool:
            context =  mActivity.getApplicationContext()
            SERVICE_NAME = str(context.getPackageName()) +\
                '.Service' + 'Tester'
            self.service = autoclass(SERVICE_NAME)
            return True

    @Platform.android
    def stop_service(self) -> bool:
        self.service.stop(mActivity)
        return True

    @Platform.android
    def start_service(self) -> bool:
        self.service.start(mActivity,'')
        return True