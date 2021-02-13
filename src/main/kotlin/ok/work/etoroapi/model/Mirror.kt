package ok.work.etoroapi.model

import com.fasterxml.jackson.annotation.JsonIgnoreProperties

@JsonIgnoreProperties(ignoreUnknown = true)
data class Avatar(val width: Int, val height: Int, val type: String, val url: String)

@JsonIgnoreProperties(ignoreUnknown = true)
data class Mirror(val realCID: Int, val lastName: String?, val firstName: String?, val aboutMe: String?, val avatars: List<Avatar>?)