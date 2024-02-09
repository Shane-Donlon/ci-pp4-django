# Swarms

## Features

Web application has the following pages:

- home page
- login page
- registration page
- logout page
- profile page
- edit profile page
- change password page
- report a swarm page
- about page
- Open Tickets page
- Resolved Tickets page
- Unresolved Tickets page

## Homepage

- Navigation bar with links for going between pages
- beekeeper login and sign-up
- multiple report swarms call to actions
- statistics about the company
- about the company links
- beekeeper information
- footer
  ![image of index page](documentation/assets/index-page.png)
  ![image of index page](documentation/assets/index-page-all-devices.jpg)

## report page

- Navigation bar with links for going between pages
- beekeeper login and sign-up
- progress bar
- report a swarm form

  - form validation
  - confirmation section
    ![image of report a swarm page](documentation/assets/form-errors.jpg)
    ![image of report a swarm page](documentation/assets/form-errors-part-2.jpg)
    ![image of report a swarm page](documentation/assets/confirmation-screen.jpg)

- footer
  ![image of report a swarm page](documentation/assets/report-page.png)
  ![image of report a swarm page](documentation/assets/index-page-all-devices.jpg)

## About page

- Navigation bar with links for going between pages
- beekeeper login and sign-up
- about the company information

- footer
  ![image of about page](documentation/assets/about-page.png)
  ![image of about page](documentation/assets/about-page-all-devices.jpg)

## sign-in page

- Navigation bar with links for going between pages
- sign-in form

- footer
  ![image of sign-in page](documentation/assets/sign-in-page-all-devices.jpg)

## sign-up page

- Navigation bar with links for going between pages
- sign-up form

- footer
  ![image of sign-up page](documentation/assets/sign-up-page-all-devices.jpg)

## open tickets page

- Navigation bar with links for going between pages for staff
- table with list of open tickets with detailed information and links to tickets
- filter to filter tickets by assignee or reported by first name
- if table is blank "There are no tickets to show" is shown
- modal for instructions on how to use the search bar
- footer
  ![image of open tickets page](documentation/assets/open-tickets-all-devices.jpg)
  ![image of how to use the search options](documentation/assets/how-to-use-search.jpg)

## resolved tickets page

- Navigation bar with links for going between pages for staff
- table with list of open tickets with detailed information and links to tickets
- filter to filter tickets by assignee or reported by first name
- if table is blank "There are no tickets to show" is shown
- modal for instructions on how to use the search bar
- footer
  ![image of resolved tickets page](documentation/assets/resolved-tickets-all-devices.jpg)
  ![image of how to use the search options](documentation/assets/how-to-use-search.jpg)

## unresolved tickets page

- Navigation bar with links for going between pages for staff
- table with list of open tickets with detailed information and links to tickets
- filter to filter tickets by assignee or reported by first name
- if table is blank "There are no tickets to show" is shown
- modal for instructions on how to use the search bar
- footer
  ![image of unresovled tickets page](documentation/assets/unresolved-tickets-all-devices.jpg)
  ![image of how to use the search options](documentation/assets/how-to-use-search.jpg)

## ticket page

- Navigation bar with links for going between pages for staff
- form is disabled by default and ticket boxes are needed to enable
- feedback is given to the staff member once the ticket has been updated
  ![image of success message](documentation/assets/success-message.jpg)
  ![image of error message](documentation/assets/error-message-ticket.jpg)

- admins have access to delete ppi (Personal and private information)

  - on request, they need to confirm this is the action to take
  - feedback is given once updated
    ![image of delete ppi ticket section](documentation/assets/delete-ppi-admin.jpg)
    ![image of delete ppi ticket section](documentation/assets/delete-ppi-admin-success.jpg)

- admins have access to delete a ticket

  - on request, they need to confirm this is the action to take
  - feedback is given once updated
  - page is redirected back to all open tickets
    ![image of delete  ticket section](documentation/assets/delete-ticket-admin.jpg)
    ![image of delete ticket section](documentation/assets/delete-ticket-admin-success.jpg)

- footer
  ![image of tickets page](documentation/assets/ticket-tickets-all-devices.jpg)

## logout page

- javascript automatically logs user out after, all staff see is a loading screen while this loads.
  ![image of laoding screen](documentation/assets/logout-page.jpg)
