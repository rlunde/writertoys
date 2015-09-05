// create the module and name it wt (for writertoys)
// also include ngRoute for all our routing needs
var wt = angular.module('wt', ['ngRoute']);

// configure our routes
wt.config(function($routeProvider) {

$routeProvider
        // route for the index page
        .when('/', {
                templateUrl : 'templates/index.html',
                controller  : 'mainCtrl'
        })

        // route for the FAQ page
        .when('/faq', {
        templateUrl : 'templates/faq.html',
        controller  : 'faqCtrl'
        })

        // route for the contact page
        .when('/contact', {
                templateUrl : 'templates/contact.html',
                controller  : 'contactCtrl'
        });
});

// create the controller and inject Angular's $scope
wt.controller('mainCtrl', function($scope) {
        // create a message to display in our view
        $scope.heading = 'Welcome to WriterToys';
        $scope.message = 'This is just an empty template -- nothing to see yet.';
});

wt.controller('faqCtrl', function($scope) {
        $scope.heading = 'WriterToys FAQ';
        $scope.message = 'This is where you will find stuff, when there is stuff to find.';
});

wt.controller('contactCtrl', function($scope) {
        $scope.heading = 'Contact WriterToys';
        $scope.message = 'Contact Ron Lunde:';
});
