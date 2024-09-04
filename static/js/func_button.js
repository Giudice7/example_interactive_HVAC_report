function toggleNewSection() {
    // Get the new section by its ID
    const newSection = document.getElementById('new-section');

    // Toggle visibility by adding/removing a 'd-none' class (Bootstrap hidden class)
    if (newSection.classList.contains('d-none')) {
        newSection.classList.remove('d-none');
    } else {
        newSection.classList.add('d-none');
    }
}