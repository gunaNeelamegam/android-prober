from jnius import autoclass
from android import mActivity

class AndroidService:
    """Using this class we can able to start and stop the service programmtically
    """

    def __init__(self) -> None:
        self.service = None
        self.setup_service()

    def setup_service(self) -> bool:
        """Using this method initiate the service class reference

        Returns:
            bool: False as Failure True as Successfully
        """
        status = False
        try:
            context =  mActivity.getApplicationContext()
            SERVICE_NAME = str(context.getPackageName()) +\
                '.Service' + 'Tester'
            self.service = autoclass(SERVICE_NAME)
            status = True
        except Exception as e:
            print("EXCEPTION", e.args);
        finally:
            return status

    def stop_service(self) -> bool:
        status = False
        try:
            self.service.stop(mActivity)
            status = True
        except Exception as e:
            print("EXECEPTION : ", e.args)
        finally:
            return status

    def start_service(self) -> bool:
        status = False
        try:
            self.service.start(mActivity,'')
            status = True
        except Exception as e:
            print("EXECPTION:", e.args)
        finally :
            return status
