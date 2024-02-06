Overall Plan Of Action:
Deploy early

Priority List:
Users will be the general public users for this site, and will house all the unauthenticated views.
User stories will be the first priority to get the public facing site up and running.

Moving on form user stories to the Ticket model next

Bee Keeper stories so that staff can update the tickets
Admin stories so that the admins can update the tickets.

Once all MVPs have been completed move onto the "Should haves"
Then "could haves"
Then "Won't haves"

link to site:
[Link to live site](https://ci-sd-pp4-swarms-ie-54c976de26c1.herokuapp.com/).

### bugs

#### resolved bugs

<table>
<thead>
  <tr>
    <th>Page</th>
    <th>Language</th>
    <th>Description</th>
    <th>Resolution</th>
    <th>Cause</th>

  </tr>
</thead>
<tbody>
  <tr>
    <td>Report-Swarm</td>
    <td>JavaScript</td>
    <td>Using regex on phone to confirm if number is correct, if at any point an error appeared I would set the custom error to be more descriptive than pattern does not match, once I corrected the error on change and next would still set the error and could not move onto the next section of the form
    event.target.setCustomValidity("Please enter phone number in 353121234567 format");</td>
    <td> event.target.setCustomValidity("");</td>
    <td> As I'm setting the error to true by using a non-empty sting I need to set this back to false using an empty string after the error appears </td>

  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>

  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
   
  </tr>
</tbody>
</table>
