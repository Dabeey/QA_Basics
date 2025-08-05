// ///////////////// 🚨Get and Set Variables with Scripts ///////////////


// Create global variable
pm.globals.set('name', 'Dabeey');

// Create global variable
pm.collectionVariables.set('name', 'YF Backend Girl');

// Before you do this, you have to first select an environment
pm.environment.set('name','Mercy');

// set local variable
pm.variables.set('name','daberechi');

// Get variable
let name = pm.variables.get('name'); 
console.log(name);
// Do same for other type of variable

// To remove 
pm.collectionVariables.unset('name');

// To check if variable exist
pm.collectionVariables.has('name');

// To get all variables
pm.collectionVariables.all();

// Set Header
pm.request.headers.add({key: 'Header-Name', value: 'Header-Value'});

// Get Header
let headerValue = pm.request.headers.get('Header-Name');
console.log(headerValue);

// Remove Header
pm.request.headers.remove('Header-Name');

// To check if header exist
pm.request.headers.has('Header-Name');

// To get all headers
pm.request.headers.all();

// Set Authorization
pm.request.auth.bearer().set('Bearer ' + pm.environment.get('authToken'));

// Get Authorization
let auth = pm.request.auth.bearer().get();

// Remove Authorization
pm.request.auth.bearer().unset();