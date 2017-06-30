$(document).ready(function() {
	$('#like').click(function() {
		var postId;
		postId = $(this).attr("data-post-id");
  	rate_post(postId, 'Like');
	})

	$('#dislike').click(function() {
		var postId;
		postId = $(this).attr("data-post-id");
		rate_post(postId, 'Dislike');
	})

	function rate_post(postId, action) {
		$.get('/blog/posts/rate', {post_id: postId, action: action}, function(data) {
			$('#ratio').html(data);
			$('#like').hide();
			$('#dislike').hide();
		});
	}
});