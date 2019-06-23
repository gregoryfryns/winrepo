$( document ).ready(() => {
    const MAX_SKILLS_NB = 3;
    let $skillsField = $('#div_id_skills');

    function checkSkillsCount() {
        if ($skillsField.find('.skills_checkbox:checked').length > MAX_SKILLS_NB) {
            $skillsField.find('.btn-outline-primary')
                        .removeClass('btn-outline-primary')
                        .addClass('btn-outline-danger');
            $skillsField.find('#hint_id_skills')
                        .removeClass('text-muted')
                        .addClass('text-danger');
        }
        else {
            $skillsField.find('.btn-outline-danger')
                        .removeClass('btn-outline-danger')
                        .addClass('btn-outline-primary');
            $skillsField.find('#hint_id_skills')
                        .removeClass('text-danger')
                        .addClass('text-muted');
        }
    }

    checkSkillsCount();
    
    $skillsField.find('.skills_checkbox').change(() => {
        checkSkillsCount();
    });
});
