$('#add-question').click(() => {
    const questionList = $('#question-list');
    const lastListItem = $('#question-list li').last();
    const lastInput = lastListItem.find('input');

    //clone list item
    const newListItem = lastListItem.clone();

    //clear value
    newListItem.find('input').val('');

    //update index attribute
    const name = lastInput.attr('name');
    const index = parseInt(name.split('-')[0]) + 1;
    newListItem.find('input').attr('name', `${index}-desc`);
    newListItem.find('input').attr('id', `id_${index}-desc`);

    //append
    newListItem.appendTo(questionList);
});

