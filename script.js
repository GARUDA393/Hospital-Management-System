async function fetchAndDisplay(endpoint, elementId, formatter) {
    const res = await fetch(`http://localhost:3000/${endpoint}`);
    const data = await res.json();
    const list = document.getElementById(elementId);
    data.forEach(item => {
      const li = document.createElement('li');
      li.textContent = formatter(item);
      list.appendChild(li);
    });
  }
  
  window.onload = () => {
    fetchAndDisplay('patients', 'patientList', p => `${p.name} (${p.age}, ${p.gender}) - ${p.diagnosis}`);
    fetchAndDisplay('doctors', 'doctorList', d => `${d.name} - ${d.specialty}`);
    fetchAndDisplay('appointments', 'appointmentList', a => `${a.patientName} with ${a.doctorName} on ${a.date} at ${a.time}`);
    fetchAndDisplay('facilities', 'facilityList', f => `${f.name}: ${f.description}`);
    fetchAndDisplay('news', 'newsList', n => `${n.title} (${n.date}) - ${n.summary}`);
    fetchAndDisplay('services', 'serviceList', s => `${s.name} - ₹${s.price} - ${s.availability}`);
  };