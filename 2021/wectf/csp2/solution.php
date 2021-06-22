<?php
namespace ShouFramework {
    abstract class Typed {
        abstract protected function construct();
        abstract protected function destruct();

        private function type_checker() {}

        public function __construct() {
            $this->construct();
        }

        public function __destruct() {
            $this->destruct();
        }

        public function __wakeup() {
            $this->type_checker();
        }
    }

    class Template extends Typed {
        protected function construct() {}

        protected function destruct() {}
    }

    abstract class HTTP extends Typed {
        public Template $template_object;

        protected function construct() {
            $this->template_object = new Template();
        }

        public function handle() {}

        public function handle_request() {
            $this->handle();
            $this->render();
        }

        abstract public function render();

        protected function destruct() {
            $this->handle_request();
        }
    }

    class CSP extends Typed {
        public $report_uri_string = "/a; script-src-elem 'unsafe-inline'";

        protected function construct() {}

        protected function destruct() {}
    }
}

namespace {
    class UserData extends \ShouFramework\Typed {
        public $token_string = 'test';

        protected function construct() {}

        protected function destruct() {}
    }

    class CatWithHashGet extends \ShouFramework\HTTP {
        public UserData $user_object;
        public \ShouFramework\CSP $csp_object;

        public function construct() {
            parent::construct();
            $this->user_object = new UserData();
            $this->csp_object = new \ShouFramework\CSP();
        }

        public function render() {}
    }

    echo urlencode(serialize([new CatWithHashGet])) . PHP_EOL;
}
?>